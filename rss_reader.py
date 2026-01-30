"""
Improved RSS Feed Reader with Better Summary Extraction
Handles multiple RSS formats and extracts summaries properly
"""

import requests
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
import json
from typing import List, Dict
import html

def clean_html(text: str) -> str:
    """Remove HTML tags and decode entities"""
    if not text:
        return ""
    
    # Decode HTML entities
    text = html.unescape(text)
    
    # Remove HTML tags (simple approach)
    import re
    text = re.sub(r'<[^>]+>', '', text)
    
    # Clean up whitespace
    text = ' '.join(text.split())
    
    return text[:300]  # Limit to 300 chars

def fetch_feed(url: str, hours_back: int = 24) -> List[Dict]:
    """
    Fetch and parse RSS feed with improved summary extraction
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(url, timeout=15, headers=headers)
        response.raise_for_status()
        
        # Parse XML
        root = ET.fromstring(response.content)
        
        items = []
        
        # Try RSS 2.0 format first
        for item in root.findall('.//item')[:10]:
            title_elem = item.find('title')
            link_elem = item.find('link')
            
            # Try multiple summary fields
            summary = ""
            for field in ['description', 'summary', 'content:encoded', '{http://purl.org/rss/1.0/modules/content/}encoded']:
                summary_elem = item.find(field)
                if summary_elem is not None and summary_elem.text:
                    summary = clean_html(summary_elem.text)
                    break
            
            # If still no summary, try text content of description
            if not summary:
                desc_elem = item.find('description')
                if desc_elem is not None:
                    summary = clean_html(desc_elem.text or "")
            
            pub_date_elem = item.find('pubDate')
            
            if title_elem is not None and link_elem is not None:
                items.append({
                    'title': clean_html(title_elem.text or 'No title'),
                    'link': link_elem.text or '',
                    'summary': summary or 'No summary available',
                    'published': pub_date_elem.text if pub_date_elem is not None else 'Unknown'
                })
        
        # Try Atom format if no items found
        if not items:
            atom_ns = '{http://www.w3.org/2005/Atom}'
            for entry in root.findall(f'.//{atom_ns}entry')[:10]:
                title_elem = entry.find(f'{atom_ns}title')
                link_elem = entry.find(f'{atom_ns}link')
                
                # Try multiple summary fields for Atom
                summary = ""
                for field in [f'{atom_ns}summary', f'{atom_ns}content']:
                    summary_elem = entry.find(field)
                    if summary_elem is not None and summary_elem.text:
                        summary = clean_html(summary_elem.text)
                        break
                
                updated_elem = entry.find(f'{atom_ns}updated')
                
                if title_elem is not None:
                    link_href = link_elem.get('href') if link_elem is not None else ''
                    items.append({
                        'title': clean_html(title_elem.text or 'No title'),
                        'link': link_href,
                        'summary': summary or 'No summary available',
                        'published': updated_elem.text if updated_elem is not None else 'Unknown'
                    })
        
        return items[:10]
        
    except requests.exceptions.Timeout:
        print(f"⏱️  Timeout")
        return []
    except requests.exceptions.HTTPError as e:
        if '429' in str(e):
            print(f"⏸️  Rate limited")
        elif '404' in str(e):
            print(f"❌ 404")
        else:
            print(f"❌ HTTP {e}")
        return []
    except Exception as e:
        print(f"⚠️  {str(e)[:30]}")
        return []

def aggregate_all_feeds(sources_json: str = 'content_sources.json', hours_back: int = 24) -> Dict:
    """
    Aggregate content from all configured sources with better error handling
    """
    
    try:
        with open(sources_json, 'r', encoding='utf-8') as f:
            sources = json.load(f)
    except FileNotFoundError:
        print(f"❌ Error: {sources_json} not found!")
        print("   Run 'python setup.py' first")
        return {}
    
    all_content = {}
    total_items = 0
    total_with_summaries = 0
    
    print("\n📡 Fetching RSS feeds with summaries...\n")
    
    for source in sources:
        category = source['category']
        name = source['name']
        url = source['url']
        
        print(f"  {name:30} ", end='')
        items = fetch_feed(url, hours_back)
        
        if items:
            # Count items with actual summaries
            with_summaries = sum(1 for item in items if item['summary'] != 'No summary available')
            print(f"✅ ({len(items)} items, {with_summaries} with summaries)")
            total_items += len(items)
            total_with_summaries += with_summaries
        else:
            print("")
        
        if category not in all_content:
            all_content[category] = {}
        
        all_content[category][name] = items
    
    print(f"\n📊 Results:")
    print(f"   Total items: {total_items}")
    print(f"   With summaries: {total_with_summaries}")
    print(f"   Without summaries: {total_items - total_with_summaries}")
    
    return all_content

def main():
    """Main function"""
    
    print("\n" + "="*70)
    print("  IMPROVED RSS FEED AGGREGATOR")
    print("="*70)
    
    # Check if sources file exists
    import os
    if not os.path.exists('content_sources.json'):
        print("\n❌ Error: content_sources.json not found!")
        print("   Please run 'python setup.py' first")
        return
    
    # Fetch feeds
    content = aggregate_all_feeds(hours_back=168)  # Last week for better summaries
    
    if not content:
        print("\n⚠️  No content fetched")
        return
    
    # Save to file
    try:
        with open('aggregated_content.json', 'w', encoding='utf-8') as f:
            json.dump(content, f, indent=2, ensure_ascii=False)
        
        print(f"\n✅ Saved to: aggregated_content.json")
        
        # Print detailed summary
        print("\n📊 Summary by Category:")
        for category, sources in content.items():
            total = sum(len(items) for items in sources.values())
            with_summaries = sum(
                sum(1 for item in items if item['summary'] != 'No summary available')
                for items in sources.values()
            )
            print(f"  {category:15} : {total:3} items ({with_summaries:3} with summaries)")
        
        # Show sample with summary
        print("\n📝 Sample Item with Summary:")
        for category, sources in content.items():
            for source_name, items in sources.items():
                for item in items:
                    if item['summary'] and item['summary'] != 'No summary available':
                        print(f"\n  Source: {source_name}")
                        print(f"  Title: {item['title'][:60]}...")
                        print(f"  Summary: {item['summary'][:150]}...")
                        print(f"  Link: {item['link']}")
                        break
                if any(item['summary'] != 'No summary available' for item in items):
                    break
            if any(any(item['summary'] != 'No summary available' for item in items) for items in sources.values()):
                break
        
        print("\n" + "="*70)
        print("  COMPLETE!")
        print("="*70)
        print("\nNext steps:")
        print("  1. Review: aggregated_content.json")
        print("  2. Run: python run_daily.py")
        print("  3. Create posts using the dashboard")
        
    except Exception as e:
        print(f"\n❌ Error saving: {e}")

if __name__ == "__main__":
    main()