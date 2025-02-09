import streamlit as st
from example_functions.domain_adaptation_streamlit_example import domain_adaptation_example
from example_functions.video_loading_streamlit_example import demo_1, demo_2, demo_3, demo_4
from streamlit_card import card


examples = [
    {
        "name": "Video Loading Example",
        "description": "Some Description",
        "image": "http://placekitten.com/500/500",
        "nav": "video_example"
    },
    
    {
        "name": "Domain Adaptation Example",
        "description": "Some Description",
        "image": "http://placekitten.com/500/500",
        "nav": "domain_adaptation"
    },

    {
        "name": "Third Example",
        "description": "Some Description",
        "image": "http://placekitten.com/500/500",
        "nav": "domain_adaptation"
    },

    {
        "name": "Fourth Example",
        "description": "Some Description",
        "image": "http://placekitten.com/500/500",
        "nav": "domain_adaptation"
    },

    {
        "name": "Fifth Example",
        "description": "Some Description",
        "image": "http://placekitten.com/500/500",
        "nav": "domain_adaptation"
    },

    {
        "name": "Sixth Example",
        "description": "Some Description",
        "image": "http://placekitten.com/500/500",
        "nav": "domain_adaptation"
    }
]

def go_to(page):
    st.session_state["page"] = page


def home_page():
    # Title
    st.markdown("<h1 style='text-align: center;'>Welcome To The Pykale Example Archive 👋</h1>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center;'>Here we explore some examples created in pykale</h5>", unsafe_allow_html=True)

    # Grid Layout For Examples
    for row in range(0, len(examples), 3):
        cols = st.columns(3)

        for i in range(3):
            if row + i < len(examples):
                example = examples[row+i]

                with cols[i]:
                    card(
                        title=example["name"],
                        text=example["description"],
                        image=example["image"],
                        styles = {
                            "card": {
                                "width": "100%"
                            }
                        },
                        on_click=lambda nav=example["nav"]: go_to(nav)
                    )


def video_demo_page():
    # Title
    st.button("Back to Home", on_click=go_to, args=("home",))
    st.markdown("<h1 style='text-align: center;'>Video Loading Example</h1>", unsafe_allow_html=True)


    # Demo button
    demo = st.radio(
        "Select Demo To Try Out",
        ["Demo 1",  "Demo 2", "Demo 3", "Demo 4"],
        index=None
    )
    
    # state management
    if demo == "Demo 1":
        demo_1()
    elif demo == "Demo 2":
        demo_2()
    elif demo == "Demo 3":
        demo_3()
    elif demo == "Demo 4":
        demo_4()

def domain_adaptation_page():
    st.button("Back to Home", on_click=go_to, args=("home",))
    st.markdown("<h1 style='text-align: center;'>Domain Adaptation Example</h1>", unsafe_allow_html=True)
    domain_adaptation_example()
