import streamlit as st

def render_header():
    """Render the shared header component."""
    st.markdown("""
    <div style="background-color: #f0f2f6; padding: 1rem; margin-bottom: 2rem; border-radius: 0.5rem;">
        <h1 style="color: #0e1117; margin: 0;">🔍 Sitemap Explorer</h1>
        <p style="color: #4a4a4a; margin-top: 0.5rem;">
            Professional XML Sitemap Analysis Tool
        </p>
        <nav style="margin-top: 1rem;">
            <a href="/" target="_self" style="text-decoration: none; color: #0e1117; margin-right: 1rem;">Home</a>
            <a href="/app/sitemap_extractor" target="_self" style="text-decoration: none; color: #0e1117;">Sitemap Extractor</a>
        </nav>
    </div>
    """, unsafe_allow_html=True)
