import streamlit as st

def go_to(page):
    """Navigate to a given page."""
    st.session_state["page"] = page
    st.rerun()


def navbar():
    """Sidebar navigation menu."""
    st.sidebar.title("Navigation")

    nav_items = {
        "🏠 Home": "home",
        "🎓 Learning Hub": "hub",
        "💬 PyKale Assistant": "chatbot_page",
        "⚙️ Train a Model": "train_page",
    }

    for label, route_key in nav_items.items():
        if st.sidebar.button(label, key=f"nav_{route_key}"):
            go_to(route_key)
