import streamlit as st
from navigation.navigation import go_to
from streamlit_card import card
from utils.constants import HUB
from views.components.ui import page_header


def hub_page():    
    """Hub page"""
    # Header
    page_header(
        title="Welcome To The Learning Hub 🎓",
        subtitle="Explore guides, tutorials, and interactive demos to understand PyKale better."
    )
    
    # Category Filter
    all_categories = sorted(list({ex["category"] for ex in HUB}))
    all_categories.insert(0, "All") 
    selected_category = st.selectbox("Select a category:", all_categories, index=0)

    # Search
    search_query = st.text_input("Search Guides & Tutorials:", value="", key="hub_search")

    # Filter
    filtered_modules = []
    for module in HUB:
        if selected_category != "All" and module["category"] != selected_category:
            continue

        if search_query:
            combined_text = (module["name"] + " " + module["description"]).lower()
            if search_query.lower() not in combined_text:
                continue

        filtered_modules.append(module)


    # Display filtered results
    num_cols = 3 
    cols = st.columns(num_cols)

    if not filtered_modules:
        st.write("No matching tutorials found.")
        return

    for i, module in enumerate(filtered_modules):
        with cols[i % num_cols]:
            card(
                title=module["name"],
                text=module["description"],
                image=module["image"],
                styles={
                    "card": {
                        "width": "100%",
                        "padding": "15px",
                        "border-radius": "10px",
                        "box-shadow": "0px 4px 8px rgba(0,0,0,0.2)",
                    }
                },
                on_click=lambda nav=module["nav"]: go_to(nav),
                key=f"card_{i}"
            )
