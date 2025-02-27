import streamlit as st

def go_to(page):
    """Updates session state to navigate between pages."""
    st.session_state["page"] = page
    st.rerun()

def navbar():
    """Sidebar navigation menu for switching pages."""
    st.sidebar.title("Navigation")
    if st.sidebar.button("🏠 Home", key="nav_home"):
        go_to("home")
    if st.sidebar.button("📚 Learning Hub", key="nav_hub"):
        go_to("hub")
