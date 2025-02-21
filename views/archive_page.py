import streamlit as st
from streamlit_card import card
from helpers.constants import EXAMPLES
from navigation import go_to


def archive_page():    
    st.markdown("<h1 style='text-align: center;'>Welcome To The Pykale Example Archive 👋</h1>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center;'>Here we explore some examples created in Pykale</h5>", unsafe_allow_html=True)

    # Category Filter
    all_categories = sorted(list({ex["category"] for ex in EXAMPLES}))
    all_categories.insert(0, "All")  # "All" option at the top
    selected_category = st.selectbox("Select a category to filter examples:", all_categories, index=0)

    # Search
    search_query = st.text_input("Search Examples by Name or Description:", value="", key="archive_search")

    # Filter
    filtered_examples = []
    for ex in EXAMPLES:
        # Category match
        if selected_category != "All" and ex["category"] != selected_category:
            continue

        # Search match
        if search_query:
            # If user typed something, we do a case-insensitive match on name or description
            combined_text = (ex["name"] + " " + ex["description"]).lower()
            if search_query.lower() not in combined_text:
                continue

        filtered_examples.append(ex)


    # Display filtered examples
    num_cols = 3  # Cards per row
    cols = st.columns(num_cols)

    # If no examples found, show a friendly message
    if not filtered_examples:
        st.write("No examples match your filter. Try changing category or search.")
        return

    for i, example in enumerate(filtered_examples):
        with cols[i % num_cols]:
            card(
                title=example["name"],
                text=example["description"],
                image=example["image"],
                styles={
                    "card": {
                        "width": "100%",
                        "padding": "15px",
                        "border-radius": "10px",
                        "box-shadow": "0px 4px 8px rgba(0,0,0,0.2)",
                    }
                },
                on_click=lambda nav=example["nav"]: go_to(nav),
                key=f"card_{i}"
            )
