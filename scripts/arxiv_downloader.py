#!/usr/bin/env python3
"""
ArXiv paper downloader with metadata extraction
"""
import re
import os
import sys
import json
import time
import argparse
import requests
from typing import Dict, Optional, List
from datetime import datetime
import xml.etree.ElementTree as ET
from pathlib import Path

class ArxivDownloader:
    def __init__(self, base_dir: str = "../papers"):
        self.base_dir = Path(base_dir)
        self.raw_dir = self.base_dir / "raw"
        self.metadata_dir = self.base_dir / "metadata"
        self.processed_dir = self.base_dir / "processed"
        
        # Create directories if needed
        for dir_path in [self.raw_dir, self.metadata_dir, self.processed_dir]:
            dir_path.mkdir(parents=True, exist_ok=True)
        
        self.arxiv_api = "http://export.arxiv.org/api/query"
        self.headers = {
            'User-Agent': 'Research Paper Downloader/1.0'
        }
    
    def search_papers(self, query: str, max_results: int = 10) -> List[Dict]:
        """Search ArXiv for papers matching query"""
        params = {
            'search_query': query,
            'start': 0,
            'max_results': max_results,
            'sortBy': 'relevance',
            'sortOrder': 'descending'
        }
        
        print(f"Searching ArXiv for: {query}")
        response = requests.get(self.arxiv_api, params=params)
        
        if response.status_code != 200:
            print(f"Error searching ArXiv: {response.status_code}")
            return []
        
        root = ET.fromstring(response.text)
        papers = []
        
        # Parse XML namespace
        ns = {'arxiv': 'http://www.w3.org/2005/Atom'}
        
        for entry in root.findall('arxiv:entry', ns):
            paper = self._parse_arxiv_entry(entry, ns)
            papers.append(paper)
            
        return papers
    
    def _parse_arxiv_entry(self, entry, ns) -> Dict:
        """Parse single ArXiv entry from XML"""
        # Extract ID from the URL
        id_elem = entry.find('arxiv:id', ns)
        arxiv_id = id_elem.text if id_elem is not None else ""
        
        # Clean the ID (remove version if present)
        arxiv_id = arxiv_id.replace("http://arxiv.org/abs/", "")
        
        # Extract other metadata
        title = entry.find('arxiv:title', ns)
        title_text = title.text.strip() if title is not None else "Unknown"
        
        summary = entry.find('arxiv:summary', ns)
        summary_text = summary.text.strip() if summary is not None else ""
        
        # Extract authors
        authors = []
        for author in entry.findall('arxiv:author', ns):
            name = author.find('arxiv:name', ns)
            if name is not None:
                authors.append(name.text)
        
        # Extract categories
        categories = []
        for cat in entry.findall('arxiv:category', ns):
            categories.append(cat.get('term', ''))
        
        # Extract dates
        published = entry.find('arxiv:published', ns)
        pub_date = published.text if published is not None else ""
        
        updated = entry.find('arxiv:updated', ns)
        update_date = updated.text if updated is not None else ""
        
        # Extract PDF link
        pdf_link = None
        for link in entry.findall('arxiv:link', ns):
            if link.get('type') == 'application/pdf':
                pdf_link = link.get('href')
                break
        
        if not pdf_link and arxiv_id:
            pdf_link = f"http://arxiv.org/pdf/{arxiv_id}.pdf"
        
        return {
            'arxiv_id': arxiv_id,
            'title': title_text,
            'authors': authors,
            'summary': summary_text,
            'categories': categories,
            'published': pub_date,
            'updated': update_date,
            'pdf_url': pdf_link
        }
    
    def download_paper(self, paper: Dict, overwrite: bool = False) -> Optional[str]:
        """Download paper PDF and save metadata"""
        arxiv_id = paper['arxiv_id'].replace('/', '_')
        pdf_path = self.raw_dir / f"{arxiv_id}.pdf"
        metadata_path = self.metadata_dir / f"{arxiv_id}.json"
        
        # Check if already exists
        if pdf_path.exists() and not overwrite:
            print(f"Paper already downloaded: {arxiv_id}")
            return str(pdf_path)
        
        # Download PDF
        pdf_url = paper['pdf_url']
        if not pdf_url:
            print(f"No PDF URL for paper: {arxiv_id}")
            return None
        
        print(f"Downloading: {paper['title'][:60]}...")
        
        try:
            response = requests.get(pdf_url, headers=self.headers, stream=True)
            response.raise_for_status()
            
            # Save PDF
            with open(pdf_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            # Save metadata
            paper['download_date'] = datetime.now().isoformat()
            paper['file_path'] = str(pdf_path)
            
            with open(metadata_path, 'w') as f:
                json.dump(paper, f, indent=2)
            
            print(f"Saved: {pdf_path}")
            return str(pdf_path)
            
        except requests.RequestException as e:
            print(f"Error downloading paper: {e}")
            return None
        
        # Rate limit
        time.sleep(1)
    
    def download_by_id(self, arxiv_id: str) -> Optional[str]:
        """Download specific paper by ArXiv ID"""
        # Clean the ID
        arxiv_id = arxiv_id.replace("arxiv:", "").strip()
        
        # Search for the specific paper
        papers = self.search_papers(f"id:{arxiv_id}", max_results=1)
        
        if not papers:
            print(f"Paper not found: {arxiv_id}")
            return None
        
        return self.download_paper(papers[0])
    
    def batch_download(self, query: str, max_papers: int = 10):
        """Download multiple papers matching query"""
        papers = self.search_papers(query, max_results=max_papers)
        
        print(f"Found {len(papers)} papers")
        
        downloaded = []
        for i, paper in enumerate(papers, 1):
            print(f"\n[{i}/{len(papers)}] Processing...")
            result = self.download_paper(paper)
            if result:
                downloaded.append(result)
            time.sleep(1)  # Be respectful to the server
        
        print(f"\nDownloaded {len(downloaded)} papers successfully")
        return downloaded

def main():
    parser = argparse.ArgumentParser(description="Download papers from ArXiv")
    parser.add_argument("query", help="Search query or ArXiv ID")
    parser.add_argument("-n", "--number", type=int, default=10,
                        help="Number of papers to download (default: 10)")
    parser.add_argument("-i", "--id", action="store_true",
                        help="Treat query as ArXiv ID")
    parser.add_argument("-o", "--overwrite", action="store_true",
                        help="Overwrite existing files")
    
    args = parser.parse_args()
    
    downloader = ArxivDownloader()
    
    if args.id:
        # Download specific paper by ID
        result = downloader.download_by_id(args.query)
        if result:
            print(f"Successfully downloaded: {result}")
    else:
        # Search and download multiple papers
        downloader.batch_download(args.query, max_papers=args.number)

if __name__ == "__main__":
    main()