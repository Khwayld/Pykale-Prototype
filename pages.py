import streamlit as st
from chatbot import display_chatbot
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
    st.write("---")
    st.subheader("Chat with Our PyKale Bot")
    display_chatbot()




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
    primary_color = "#16a085"

    
    # Title
    st.markdown(
        f"""
        <div style="
            background-color: {primary_color};
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            text-align: center;
        ">
            <h1 style="color: white; margin: 0;">📽️ Video Loading Example</h1>
            <p style="color: #ecf0f1; font-size: 18px; margin: 5px 0 0;">
                Explore how PyKale loads and transforms video frames
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # 1. Overview
    st.markdown(f"""
    <h2 style="text-align:center; color:{primary_color};">1. Overview & Why It Matters</h2>
    <p style="text-align:center; font-size:16px;">
        Short video clips can be turned into frames for deeper analysis. 
        For example, you can detect movement or classify actions in each 
        sequence of frames. 
    </p>
    """, unsafe_allow_html=True)

    st.markdown("<hr style='border:1px solid #bdc3c7;'>", unsafe_allow_html=True)


    # 2. How It Works
    st.markdown(f"""
    <h2 style="text-align:center; color:{primary_color};">2. How It Works</h2>
    <div style="display:flex; justify-content:center;">
        <ol style="list-style:none; padding-left:0;">
          <li style="margin-bottom:10px;">
            <span style="font-size:24px;">👀</span>
            <strong style="font-size:16px;">Load the Video Dataset</strong><br/>
            <span style="color:#7f8c8d;">Extract frames from each clip.</span>
          </li>
          <li style="margin-bottom:10px;">
            <span style="font-size:24px;">🧩</span>
            <strong style="font-size:16px;">Choose Sampling Strategy</strong><br/>
            <span style="color:#7f8c8d;">Pick Sparse or Continuous frames.</span>
          </li>
          <li style="margin-bottom:10px;">
            <span style="font-size:24px;">🎨</span>
            <strong style="font-size:16px;">Visualize the Frames</strong><br/>
            <span style="color:#7f8c8d;">See them below in Streamlit.</span>
          </li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr style='border:1px solid #bdc3c7;'>", unsafe_allow_html=True)

    # 3. Interactive Demo
    st.markdown(f"""
    <h2 style="text-align:center; color:{primary_color};">3. Interactive Demo</h2>
    <p style="text-align:center;">
      Select a sampling or transformation method:
    </p>
    """, unsafe_allow_html=True)



    col1, col2, col3 = st.columns([1.45,1,1])
    with col2:
        demo = st.radio(
            "",
            ["Sparse Sampling", "Continuous Frames", "Transforms & Tensors", "Multi-Label Example"],
            label_visibility="collapsed",  
            index=None,
            horizontal=False
        )
    
    st.write("---")

    if demo == "Sparse Sampling":
        demo_1()
    elif demo == "Continuous Frames":
        demo_2()
    elif demo == "Transforms & Tensors":
        demo_3()
    elif demo == "Multi-Label Example":
        demo_4()

    if demo:
        st.markdown("<hr style='border:1px solid #bdc3c7;'>", unsafe_allow_html=True)


    # 4. Under the Hood
    st.markdown(f"<h2 style='text-align:center; color:{primary_color};'>4. Under the Hood</h2>", unsafe_allow_html=True)
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

    st.markdown("<hr style='border:1px solid #bdc3c7;'>", unsafe_allow_html=True)

    # 5. Key takeaways 
    st.markdown(f"""
    <h2 style="text-align:center; color:{primary_color};">5. Key Takeaways & Next Steps</h2>
    <div style="display:flex; justify-content:center;">
      <ul style="list-style:none; padding-left:0; text-align:left; max-width:500px;">
        <li style="margin-bottom:10px;">
          <span style="font-size:24px; margin-right:8px;">💡</span>
          <strong>Sparse Sampling</strong><br/>
          Grab frames quickly without reading them all.
        </li>
        <li style="margin-bottom:10px;">
          <span style="font-size:24px; margin-right:8px;">📈</span>
          <strong>Continuous Frames</strong><br/>
          Keep consecutive frames for smoother motion analysis.
        </li>
        <li style="margin-bottom:10px;">
          <span style="font-size:24px; margin-right:8px;">🧰</span>
          <strong>Transforms & Tensors</strong><br/>
          Make frames ready for deep learning.
        </li>
        <li style="margin-bottom:10px;">
          <span style="font-size:24px; margin-right:8px;">👥</span>
          <strong>Multi-Label</strong><br/>
          Each clip can hold multiple labels (verb, noun, action).
        </li>
      </ul>
    </div>
    <div style="text-align:center; margin-top:20px;">
      <p style="color:#7f8c8d;">
        📖 <strong>Learn More:</strong> 
        <a href="https://pykale.readthedocs.io/" target="_blank" style="color:#2980b9;">
          PyKale Documentation
        </a>
      </p>
    </div>
    """, unsafe_allow_html=True)



def domain_adaptation_page():
    st.title("Domain Adaptation Example")
    domain_adaptation_example()
