import requests
import xml.etree.ElementTree as ET
from typing import List, Optional
import pandas as pd
from urllib.parse import urlparse

def validate_url(url: str) -> bool:
    """Validate if the given URL is properly formatted."""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

def fetch_sitemap(url: str) -> Optional[str]:
    """Fetch sitemap content from URL with error handling."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException:
        return None

def parse_sitemap(xml_content: str) -> List[str]:
    """Parse XML sitemap and extract URLs."""
    urls = []
    try:
        root = ET.fromstring(xml_content)
        # Handle both standard sitemaps and sitemap index files
        namespaces = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        
        # Try to find URLs in standard sitemap
        locations = root.findall('.//ns:loc', namespaces)
        
        if locations:
            urls = [loc.text for loc in locations if loc.text]
            
    except ET.ParseError:
        return []
    
    return urls

def filter_urls_by_keyword(urls: List[str], keyword: str) -> List[str]:
    """Filter URLs based on keyword."""
    if not keyword:
        return urls
    keyword = keyword.lower()
    return [url for url in urls if keyword in url.lower()]

def create_dataframe(urls: List[str]) -> pd.DataFrame:
    """Create a DataFrame from URLs."""
    return pd.DataFrame(urls, columns=['URL'])
