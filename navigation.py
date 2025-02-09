import streamlit as st

def go_to(page):
    """Updates session state to navigate between pages."""
    st.session_state["page"] = page
    st.rerun()

def navbar():
    """Sidebar navigation menu for switching pages."""
    st.sidebar.title("Navigation")
    if st.sidebar.button("Home Page 🏠", key="nav_home"):
        go_to("home")
    if st.sidebar.button("Archive Page 📚", key="nav_archive"):
        go_to("archive")
