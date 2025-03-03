import streamlit as st
from navigation import go_to
from streamlit_card import card

def kale_api_page():
    """The KALE API - Detailed Breakdown of how it works"""

    # 📌 Introduction
    st.markdown(
        """
        <div style="text-align:center;">
            <h2>📌 The KALE API Guide</h2>
            <p style="font-size:18px;">
                PyKale follows a modular, pipeline-based approach to machine learning.
                Each module below represents a specific step in the workflow.
                Click on a module to learn more.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    col_left, col_center, col_right = st.columns([3, 1, 3])
    with col_center:
        if st.button("🔙 Back to Hub"):
            go_to("hub")


    st.write("---")

    # Define API modules with descriptions
    modules = [
        {"name": "📂 Data Handling (loaddata)", "desc": "Load and manage datasets (images, videos, graphs).", "nav": "loaddata_page"},
        {"name": "⚙️ Data Preprocessing (prepdata)", "desc": "Transform raw data for modeling.", "nav": "prepdata_page"},
        {"name": "📑 Feature Extraction (embed)", "desc": "Extract feature representations using embeddings.", "nav": "embed_page"},
        {"name": "🔍 Model Prediction (predict)", "desc": "Build and apply ML models for predictions.", "nav": "predict_page"},
        {"name": "📊 Evaluation (evaluate)", "desc": "Measure performance using evaluation metrics.", "nav": "evaluate_page"},
        {"name": "🔎 Interpretation (interpret)", "desc": "Visualize and explain model decisions.", "nav": "interpret_page"},
        {"name": "🔗 Pipeline (pipeline)", "desc": "Combine all steps into a unified workflow.", "nav": "pipeline_page"},
    ]

    # Section header
    st.markdown(
        """
        <div style="text-align:center;">
            <h3>Select a Module to Explore</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Display module cards in a centered layout with 2 cards per row
    num_cols = 2
    cols = st.columns(num_cols)
    for i, module in enumerate(modules):
        with cols[i % num_cols]:
            card(
                title=module["name"],
                text=module["desc"],
                image="",
                styles={
                    "card": {
                        "width": "100%",
                        "padding": "15px",
                        "border-radius": "10px",
                        "box-shadow": "0px 4px 8px rgba(0,0,0,0.2)",
                        "cursor": "pointer"  # indicate clickable
                    }
                },
                on_click=lambda nav=module["nav"]: go_to(nav),
                key=module["nav"]
            )

    st.write("---")

    # Next Steps Section
    st.markdown(
        """
        <div style="text-align:center;">
            <h3>🚀 Next Steps</h3>
            <p>Learn more about PyKale and start implementing:</p>
            <ul style="display: inline-block; text-align: left;">
                <li>📖 <a href="https://pykale.readthedocs.io/" target="_blank">PyKale Documentation</a></li>
                <li>🔬 <a href="https://github.com/pykale/pykale" target="_blank">GitHub Repository</a></li>
                <li>📊 <a href="full_example_page" target="_self">Try a Full Example</a></li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
