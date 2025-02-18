import streamlit as st
from components.header import render_header
from components.footer import render_footer

def main():
    # Page configuration
    st.set_page_config(
        page_title="Sitemap Explorer - XML Sitemap Analysis Tool",
        page_icon="🔍",
        layout="wide"
    )

    # Render header
    render_header()

    # Hero Section
    st.markdown("""
    <div style="text-align: center; padding: 3rem 0;">
        <h1 style="font-size: 3rem; margin-bottom: 1rem;">Explore Your Website's Structure</h1>
        <p style="font-size: 1.2rem; color: #4a4a4a; margin-bottom: 2rem;">
            Extract, analyze, and optimize your website's sitemap with our powerful tools
        </p>
        <a href="/app/sitemap_extractor" style="
            background-color: #FF4B4B;
            color: white;
            padding: 0.8rem 2rem;
            border-radius: 0.5rem;
            text-decoration: none;
            font-weight: bold;
        ">Get Started →</a>
    </div>
    """, unsafe_allow_html=True)

    # Features Section
    st.markdown("""
    <h2 id="features" style="text-align: center; margin: 3rem 0;">Key Features</h2>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        ### 🔍 URL Extraction
        Extract all URLs from your XML sitemap with a single click. Support for both simple and index sitemaps.
        """)

    with col2:
        st.markdown("""
        ### 🔎 Smart Search
        Filter URLs using keywords to find exactly what you're looking for in your sitemap structure.
        """)

    with col3:
        st.markdown("""
        ### 📊 Export & Analysis
        Export your sitemap data to CSV for further analysis and integration with other tools.
        """)

    # About Section
    st.markdown("""
    <h2 id="about" style="text-align: center; margin: 3rem 0;">About Sitemap Explorer</h2>
    <p style="text-align: center; max-width: 800px; margin: 0 auto; color: #4a4a4a;">
        Sitemap Explorer is a professional tool designed to help webmasters, SEO specialists, and developers
        analyze and optimize their website structure through XML sitemap analysis. Our tool makes it easy
        to extract, search, and export sitemap data for better website management.
    </p>
    """, unsafe_allow_html=True)

    # Contact Section
    st.markdown("""
    <h2 id="contact" style="text-align: center; margin: 3rem 0;">Get in Touch</h2>
    <p style="text-align: center; color: #4a4a4a;">
        Have questions or suggestions? We'd love to hear from you!
    </p>
    """, unsafe_allow_html=True)

    # Render footer
    render_footer()

if __name__ == "__main__":
    main()
