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
    # Title
    st.markdown(
        "<h1 style='text-align: center;'>📽️ Video Loading Example</h1>", 
        unsafe_allow_html=True
    )

    st.markdown("""
    <p style="text-align:center; font-size:18px;">
    Explore how PyKale loads and transforms video frames
    </p>
    """, unsafe_allow_html=True)

    st.write("---")

    # 1. Overview
    st.markdown("<h3 style='text-align:center;'>1. Overview & Why It Matters</h3>", unsafe_allow_html=True)
    
    st.markdown("""
    <p style="text-align:center; font-size:16px;">
    This demo shows how short video clips can be loaded and processed. 
    Non-technical explanation: We take videos, split them into frames, and optionally 
    transform them for tasks like classification or motion analysis.
    </p>
    """, unsafe_allow_html=True)

    st.write("---")

    # 2. How It Works
    st.markdown("<h3 style='text-align:center;'>2. How It Works</h3>", unsafe_allow_html=True)
    st.markdown(
        """
        <div style="text-align: center;">
            1️⃣ **Load the video dataset** → Extract frames  <br><br>
            2️⃣ **Apply different sampling strategies** → Sparse, Continuous, or Transforms  <br><br>
            3️⃣ **Visualize the frames** → We show them below in Streamlit
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("---")

    # 3. Interactive Demo
    st.markdown("<h3 style='text-align:center;'>3. Interactive Demo</h3>", unsafe_allow_html=True)
    
    st.markdown("""
    <p style="text-align:center; font-size:16px;">
    Choose a sampling or transformation method:
    </p>
    """, unsafe_allow_html=True)



    col1, col2, col3 = st.columns([1.45,1,1])
    with col2:
        demo = st.radio(
            "",
            ["Sparse Sampling (Demo 1)", "Continuous Frames (Demo 2)", "Transforms & Tensors (Demo 3)", "Multi-Label Example (Demo 4)"],
            label_visibility="collapsed",  
            index=None,
            horizontal=False
        )
    
    st.write("---")


    if demo == "Sparse Sampling (Demo 1)":
        demo_1()
    elif demo == "Continuous Frames (Demo 2)":
        demo_2()
    elif demo == "Transforms & Tensors (Demo 3)":
        demo_3()
    elif demo == "Multi-Label Example (Demo 4)":
        demo_4()

    # 4. Under the Hood
    st.write("---")
    st.header("4. Under the Hood")
    with st.expander("Show Common Video Loading Code"):
        st.code("""
            # Example snippet
            dataset = VideoFrameDataset(
                root_path="...", 
                annotationfile_path="...",
                num_segments=5,
                frames_per_segment=1,
                transform=some_transforms,
                ...
            )
        """)

    st.write("---")
    st.header("5. Key Takeaways & Next Steps")
    st.markdown("""
    - 🎯 **Sparse Sampling** → Quickly sample frames without reading all of them.  
    - 🎯 **Continuous Frames** → Keep frames in sequence for smooth motion insights.  
    - 🎯 **Transforms & Tensors** → Prep frames for deep learning.  
    - 🎯 **Multi-Label** → Some datasets have multiple labels (verb, noun, etc.).
    """)

    st.markdown("""
    <p>
    📖 Read more in the <a href="https://pykale.readthedocs.io/" target="_blank">PyKale docs</a>.
    </p>
    """, unsafe_allow_html=True)

    


def domain_adaptation_page():
    st.title("Domain Adaptation Example")
    domain_adaptation_example()
