import streamlit as st
from example_functions.domain_adaptation_streamlit_example import domain_adaptation_example
from example_functions.video_loading_streamlit_example import demo_1, demo_2, demo_3, demo_4
from streamlit_card import card
from navigation import go_to


examples = [
    {
        "name": "Video Loading Example",
        "description": "Some Description",
        "image": "",
        "nav": "video_example"
    },
    
    {
        "name": "Domain Adaptation Example",
        "description": "Some Description",
        "image": "",
        "nav": "domain_adaptation"
    },

    {
        "name": "Third Example",
        "description": "Some Description",
        "image": "",
        "nav": "domain_adaptation"
    },

    {
        "name": "Fourth Example",
        "description": "Some Description",
        "image": "",
        "nav": "domain_adaptation"
    },

    {
        "name": "Fifth Example",
        "description": "Some Description",
        "image": "",
        "nav": "domain_adaptation"
    },

    {
        "name": "Sixth Example",
        "description": "Some Description",
        "image": "",
        "nav": "domain_adaptation"
    }
]


def home_page():
    st.markdown("<h1 style='text-align: center;'>Welcome To PyKale 👋</h1>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center;'>A library built upon PyTorch for multimodal learning and transfer learning from multiple data sources</h5>", unsafe_allow_html=True)




def archive_page():
    st.markdown("<h1 style='text-align: center;'>Welcome To The Pykale Example Archive 👋</h1>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center;'>Here we explore some examples created in Pykale</h5>", unsafe_allow_html=True)


    # Ensuring a proper grid layout
    num_cols = 3  # Cards per row
    cols = st.columns(num_cols)

    for i, example in enumerate(examples):
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


def video_demo_page():
    st.markdown(
        "<h1 style='text-align: center;'>📽️ Video Loading Example</h1>", 
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="text-align: center; font-size: 18px;">
        Explore different approaches to loading videos in PyKale. 
        Select one of the demos below to see how frames are sampled, transformed, and displayed.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("---")

    st.markdown("<h3 style='text-align:center; margin-bottom: -10px;'>Choose a Demo</h3>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1.66,1,1])
    with col2:
        demo = st.radio(
            "",
            ["Demo 1", "Demo 2", "Demo 3", "Demo 4"],
            label_visibility="collapsed",  
            index=None,
            horizontal=False
        )
    
    st.write("---")





    if demo == "Demo 1":
        demo_1()
    elif demo == "Demo 2":
        demo_2()
    elif demo == "Demo 3":
        demo_3()
    elif demo == "Demo 4":
        demo_4()


def domain_adaptation_page():
    st.title("Domain Adaptation Example")
    domain_adaptation_example()
