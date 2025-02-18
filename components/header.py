import streamlit as st

def render_header():
    """Render the shared header component."""
    st.markdown("""
    <style>
        .header {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            background-color: white;
            padding: 1rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            z-index: 1000;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .nav-link {
            text-decoration: none;
            color: #0e1117;
            margin: 0 1rem;
            font-weight: 500;
            transition: color 0.2s;
        }
        .nav-link:hover {
            color: #FF4B4B;
        }
    </style>
    <div class="header">
        <h3 style="margin: 0;">🔍 Sitemap Explorer</h3>
        <nav>
            <a href="/" class="nav-link">Home</a>
            <a href="/sitemap_extractor" class="nav-link">Extract URLs</a>
        </nav>
    </div>
    <div style="margin-top: 5rem;"></div>
    """, unsafe_allow_html=True)