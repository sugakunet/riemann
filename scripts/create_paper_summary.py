#!/usr/bin/env python3
"""
Create a summary document from downloaded papers metadata
"""
import json
import os
from pathlib import Path
from datetime import datetime

def load_metadata_files(metadata_dir):
    """Load all metadata JSON files"""
    papers = []
    metadata_path = Path(metadata_dir)
    
    for json_file in metadata_path.glob("*.json"):
        try:
            with open(json_file, 'r') as f:
                metadata = json.load(f)
                papers.append(metadata)
        except Exception as e:
            print(f"Error loading {json_file}: {e}")
    
    return papers

def filter_recent_papers(papers, start_year=2020):
    """Filter papers from 2020 onwards to get more comprehensive results"""
    recent_papers = []
    truly_recent = []
    
    for paper in papers:
        pub_date = paper.get('published', '')
        if pub_date:
            try:
                year = int(pub_date[:4])
                if year >= start_year:
                    recent_papers.append(paper)
                if year >= 2024:
                    truly_recent.append(paper)
            except:
                continue
    
    # If we have few 2024-2025 papers, include more from 2020+
    if len(truly_recent) < 15:
        return recent_papers
    return truly_recent

def format_paper_entry(paper):
    """Format a single paper for the markdown document"""
    title = paper.get('title', 'Unknown Title').replace('\n', ' ')
    authors = paper.get('authors', [])
    arxiv_id = paper.get('arxiv_id', '')
    published = paper.get('published', '')
    summary = paper.get('summary', '')
    categories = paper.get('categories', [])
    
    # Format date
    date_str = ''
    if published:
        try:
            date_obj = datetime.fromisoformat(published.replace('Z', '+00:00'))
            date_str = date_obj.strftime('%Y-%m-%d')
        except:
            date_str = published[:10] if len(published) >= 10 else published
    
    # Create arxiv URL
    clean_id = arxiv_id.replace('v1', '').replace('v2', '').replace('v3', '').replace('v4', '').replace('v5', '')
    arxiv_url = f"https://arxiv.org/abs/{clean_id}"
    
    # Truncate abstract to ~200 words
    abstract_words = summary.split()
    if len(abstract_words) > 200:
        abstract = ' '.join(abstract_words[:200]) + '...'
    else:
        abstract = summary
    
    # Format categories
    cat_str = ', '.join(categories) if categories else 'N/A'
    
    entry = f"""
## {title}

**Authors:** {', '.join(authors) if authors else 'Unknown'}

**ArXiv ID:** [{arxiv_id}]({arxiv_url})

**Date:** {date_str}

**Categories:** {cat_str}

**Abstract:** {abstract.replace(chr(10), ' ').strip()}

---
"""
    
    return entry

def create_summary_document(papers, output_file):
    """Create the markdown summary document"""
    
    # Sort papers by publication date (newest first)
    papers_sorted = sorted(papers, key=lambda x: x.get('published', ''), reverse=True)
    
    # Categorize papers
    rh_papers = []
    zeta_papers = []
    l_function_papers = []
    analytic_nt_papers = []
    other_papers = []
    
    for paper in papers_sorted:
        title = paper.get('title', '').lower()
        summary = paper.get('summary', '').lower()
        text = f"{title} {summary}"
        
        if 'riemann hypothesis' in text:
            rh_papers.append(paper)
        elif 'zeta' in text and ('riemann' in text or 'zeros' in text):
            zeta_papers.append(paper)
        elif 'l-function' in text or 'l function' in text or 'dirichlet' in text:
            l_function_papers.append(paper)
        elif 'analytic number theory' in text or 'prime' in text:
            analytic_nt_papers.append(paper)
        else:
            other_papers.append(paper)
    
    # Create document content
    # Count papers by year
    year_counts = {}
    for paper in papers:
        pub_date = paper.get('published', '')
        if pub_date:
            try:
                year = int(pub_date[:4])
                year_counts[year] = year_counts.get(year, 0) + 1
            except:
                continue
    
    content = f"""# Recent Papers on Riemann Hypothesis and Related Topics

**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

**Total Papers Downloaded:** {len(papers)}

This document summarizes recent research papers related to the Riemann Hypothesis and associated areas in analytic number theory.

## Papers by Year
{chr(10).join([f'- **{year}:** {count} papers' for year, count in sorted(year_counts.items(), reverse=True)])}

## Summary Statistics

- **Riemann Hypothesis Specific:** {len(rh_papers)} papers
- **Riemann Zeta Function & Zeros:** {len(zeta_papers)} papers  
- **L-Functions & Dirichlet Series:** {len(l_function_papers)} papers
- **Analytic Number Theory:** {len(analytic_nt_papers)} papers
- **Other Related Papers:** {len(other_papers)} papers

---

# Papers by Category

"""

    # Add each category
    categories = [
        ("Riemann Hypothesis Specific", rh_papers),
        ("Riemann Zeta Function & Zeros", zeta_papers),
        ("L-Functions & Dirichlet Series", l_function_papers), 
        ("Analytic Number Theory", analytic_nt_papers),
        ("Other Related Papers", other_papers)
    ]
    
    for cat_name, cat_papers in categories:
        if cat_papers:
            content += f"\n# {cat_name}\n"
            for paper in cat_papers:
                content += format_paper_entry(paper)
    
    # Write to file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Summary document created: {output_file}")
    print(f"Total papers processed: {len(papers)}")

def main():
    # Paths
    metadata_dir = "/Users/ralph/Research/papers/metadata"
    output_file = "/Users/ralph/Research/Riemann/Recent_Riemann_Papers_2024_2025.md"
    
    print("Loading metadata files...")
    papers = load_metadata_files(metadata_dir)
    print(f"Loaded {len(papers)} papers")
    
    print("Filtering recent papers (2020+)...")
    recent_papers = filter_recent_papers(papers, 2020)
    print(f"Found {len(recent_papers)} recent papers")
    
    if len(recent_papers) < 20:
        print("Including all papers for comprehensive coverage...")
        recent_papers = papers
    
    print("Creating summary document...")
    create_summary_document(recent_papers, output_file)
    
    print("Done!")

if __name__ == "__main__":
    main()