import streamlit as st
import pandas as pd
from sitemap_utils import (
    validate_url,
    fetch_sitemap,
    parse_sitemap,
    filter_urls_by_keyword,
    create_dataframe
)

# Page configuration
st.set_page_config(
    page_title="Sitemap URL Extractor",
    page_icon="🔍",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .stAlert {
        padding: 1rem;
        margin-bottom: 1rem;
    }
    .stProgress {
        margin-top: 1rem;
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.title("🔍 Sitemap URL Extractor")
st.markdown("""
Extract URLs from XML sitemaps, search through them, and export to CSV.
Enter a sitemap URL below to get started.
""")

# Initialize session state
if 'urls' not in st.session_state:
    st.session_state.urls = []
if 'df' not in st.session_state:
    st.session_state.df = None

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

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>Made with ❤️ using Streamlit</p>
</div>
""", unsafe_allow_html=True)
