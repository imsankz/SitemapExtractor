import streamlit as st

def render_footer():
    """Render the shared footer component."""
    st.markdown("""
    <div style='text-align: center; padding: 2rem 0; color: #4a4a4a;'>
        <p>© 2025 Sitemap Explorer. Made with ❤️ using Streamlit</p>
        <div style='margin-top: 1rem;'>
            <a href="#features" style='text-decoration: none; color: #4a4a4a; margin: 0 1rem;'>Features</a>
            <a href="#about" style='text-decoration: none; color: #4a4a4a; margin: 0 1rem;'>About</a>
            <a href="#contact" style='text-decoration: none; color: #4a4a4a; margin: 0 1rem;'>Contact</a>
        </div>
    </div>
    """, unsafe_allow_html=True)