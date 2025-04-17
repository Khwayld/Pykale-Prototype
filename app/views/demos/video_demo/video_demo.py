import streamlit as st
from utils.constants import PRIMARY_COLOR

from views.demos.video_demo.demos.demo_basic import demo_basic_sampling
from views.demos.video_demo.demos.demo_continuos import demo_continuos
from views.demos.video_demo.demos.demo_transforms import demo_transforms
from views.demos.video_demo.demos.demo_multilabel import demo_multilabel

from views.components.ui import page_header, info_card, button_component

def video_demo_page():    
    """
    Main demo page for demonstrating PyKale's video loading and preprocessing capabilities.
    """
    # Header
    col_left, col_mid, col_right = st.columns([1, 4, 1])

    with col_mid:
        page_header(
            title="📽️ Video Loading with PyKale",
            subtitle="Explore how PyKale efficiently loads, samples, and transforms video frames for analysis.",
        )

        button_component(
            button_text="🔙 Back to Hub",
            slug="hub"
        )
    
    # Demo Selector
    with col_mid:
        st.markdown(f"<h2 style='text-align:center; color:{PRIMARY_COLOR};'>Try It Out</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center;'>Choose a demo to run below:</p>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1.6, 2.5, 1])
        with col2:
            demo_choice = st.radio(
                label="",
                options=[
                    "🍃 Basic Video Loading (sparse sampling)",
                    "🎞️ Continuous Clip Loading (contiguous frames)",
                    "🧰 Preprocessing Transforms (resize, normalize)",
                    "👥 Multi-Label Loading (multiple labels per clip)"
                ],
                label_visibility="collapsed"
            )

        st.markdown("---")

        # Dispatch demo
        if "Basic" in demo_choice:
            demo_basic_sampling()
        elif "Continuous" in demo_choice:
            demo_continuos()
        elif "Preprocessing" in demo_choice:
            demo_transforms()
        elif "Multi-Label" in demo_choice:
            demo_multilabel()


    # Summary
    with col_mid:
        info_card(
            title="📌 Summary & Next Steps",
            bullets=[
                "🍃 <strong>Sparse Sampling:</strong> Efficiently extracts key frames, reducing computational load while capturing essential video content.",
                "🎞️ <strong>Continuous Clips:</strong> Retrieves a contiguous sequence of frames to capture motion dynamics and context.",
                "🧰 <strong>Preprocessing Pipeline:</strong> Transforms raw frames into model-ready tensors via resizing, cropping, and normalization.",
                "👥 <strong>Multi-Label Handling:</strong> Supports video samples with multiple labels, enabling more complex annotation tasks.",
            ],
            footer_note="""
            <em>
            Experiment with these techniques to see how different sampling strategies and preprocessing steps 
            can improve your model's performance. Adjust hyperparameters and customize the transforms to suit your dataset.
            </em>
            """
        )

