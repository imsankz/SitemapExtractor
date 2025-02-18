import streamlit as st
import requests
import xml.etree.ElementTree as ET
import pandas as pd
from typing import List, Optional
from urllib.parse import urlparse

# Utility Functions
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
        namespaces = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
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

# Header Component
def render_header():
    st.markdown("""
    <style>
        .header {
            padding: 1rem 0;
            margin-bottom: 2rem;
            border-bottom: 1px solid #e5e5e5;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .app-title {
            font-size: 1.5rem;
            font-weight: bold;
            margin: 0;
            color: #0e1117;
        }
    </style>
    <div class="header">
        <h1 class="app-title">🔍 Sitemap Explorer</h1>
    </div>
    """, unsafe_allow_html=True)

# Footer Component
def render_footer():
    st.markdown("""
    <div style='text-align: center; padding: 2rem 0; color: #4a4a4a; border-top: 1px solid #e5e5e5; margin-top: 2rem;'>
        <p>© 2025 Sitemap Explorer. Made with ❤️ using Streamlit</p>
    </div>
    """, unsafe_allow_html=True)

# Main Application
def main():
    # Page configuration
    st.set_page_config(
        page_title="Sitemap URL Extractor - Sitemap Explorer",
        page_icon="🔍",
        layout="wide"
    )

    # Render header
    render_header()

    # Initialize session state
    if 'urls' not in st.session_state:
        st.session_state.urls = []
    if 'df' not in st.session_state:
        st.session_state.df = None

    # Main content
    st.markdown("""
    <div style="max-width: 800px; margin: 0 auto;">
        <h2>Extract URLs from Sitemap</h2>
        <p style="color: #4a4a4a;">
            Enter your sitemap URL below to extract all URLs. You can then search through them
            and export the results to CSV.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Input section
    sitemap_url = st.text_input(
        "Enter Sitemap URL",
        placeholder="https://example.com/sitemap.xml"
    )

    # Process sitemap
    if st.button("Extract URLs", type="primary"):
        if not sitemap_url:
            st.error("Please enter a sitemap URL")
        elif not validate_url(sitemap_url):
            st.error("Please enter a valid URL")
        else:
            with st.spinner("Fetching sitemap..."):
                xml_content = fetch_sitemap(sitemap_url)
                
                if xml_content is None:
                    st.error("Failed to fetch sitemap. Please check the URL and try again.")
                else:
                    urls = parse_sitemap(xml_content)
                    if not urls:
                        st.error("No URLs found in the sitemap or invalid sitemap format.")
                    else:
                        st.session_state.urls = urls
                        st.session_state.df = create_dataframe(urls)
                        st.success(f"Successfully extracted {len(urls)} URLs!")

    # Search and display section
    if st.session_state.urls:
        st.markdown("### Search and Export")
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            search_keyword = st.text_input(
                "Search URLs",
                placeholder="Enter keyword to filter URLs"
            )
        
        with col2:
            if st.session_state.df is not None:
                csv = st.session_state.df.to_csv(index=False)
                st.download_button(
                    label="Download CSV",
                    data=csv,
                    file_name="sitemap_urls.csv",
                    mime="text/csv",
                    key="download-csv"
                )
        
        # Filter and display URLs
        filtered_urls = filter_urls_by_keyword(st.session_state.urls, search_keyword)
        filtered_df = create_dataframe(filtered_urls)
        
        st.markdown(f"### Results ({len(filtered_urls)} URLs)")
        
        if len(filtered_urls) > 0:
            st.dataframe(
                filtered_df,
                use_container_width=True,
                height=400
            )
        else:
            st.info("No URLs match your search criteria.")

    # Render footer
    render_footer()

if __name__ == "__main__":
    main()
