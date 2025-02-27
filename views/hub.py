import streamlit as st
from streamlit_card import card
from helpers.constants import HUB
from navigation import go_to


def hub_page():    
    st.markdown("<h1 style='text-align: center;'>Welcome To The Learning Hub 🎓</h1>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center;'>Explore guides, tutorials, and interactive demos to understand PyKale better.</h5>", unsafe_allow_html=True)

    # Category Filter
    all_categories = sorted(list({ex["category"] for ex in HUB}))
    all_categories.insert(0, "All")  # "All" option at the top
    selected_category = st.selectbox("Select a category:", all_categories, index=0)

    # Search
    search_query = st.text_input("Search Guides & Tutorials:", value="", key="hub_search")

    # Filter
    filtered_modules = []
    for module in HUB:
        # Category match
        if selected_category != "All" and module["category"] != selected_category:
            continue

        # Search match
        if search_query:
            combined_text = (module["name"] + " " + module["description"]).lower()
            if search_query.lower() not in combined_text:
                continue

        filtered_modules.append(module)


    # Display filtered results
    num_cols = 3  # Cards per row
    cols = st.columns(num_cols)

    if not filtered_modules:
        st.write("No matching tutorials found. Try a different category or search.")
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
