import streamlit as st
from utils.helper_utils import load_file

from views.components.ui import (
    info_card,
    page_header,
    button_component,
    code_snippet_block
)

def prepdata_page():
    """KALE API - Data Preprocessing (kale.prepdata)"""
    # Header
    page_header(
        title="⚙️ Data Preprocessing - <code>kale.prepdata</code>",
        subtitle="""
        This module provides functions to transform and prepare raw data for machine learning models.
        It supports image, video, and other data transformations.
        """
    )
    
    button_component(
        button_text="🔙 Back to API Guide",
        slug="kale_api"
    )

    # Overview
    info_card(
        title="🔹 Overview",
        subtitle="""
        The <code>kale.prepdata</code> module offers essential tools for data preprocessing. Its main functionalities include:        
        """,
        bullets=[
            "🖼️ <strong>Image Transformations:</strong> Create transformation pipelines for tasks such as resizing, cropping, and normalizing images.",
            "🔄 <strong>Tensor Conversion:</strong> Convert lists of video frames into PyTorch tensors for efficient model processing.",
        ]
    )

    # Guide section
    col1, col2, col3 = st.columns([1, 3, 1])  
    with col2:
        code_snippet_block(
            label="🖼️ Image Transformations",
            write_up="""
            The image transformation functions in `kale.prepdata` allow you to:
            - **Resize** images to a consistent size.
            - **Crop** images to focus on important regions.
            - **Normalize** images by adjusting their pixel intensity distributions.
            One key function is `get_transform`, which creates a transformation pipeline.
            """,
            code=load_file("code_snippets/kale_api/prepdata/image_transform.py")
        )

        code_snippet_block(
            label="🔄 Tensor Conversion",
            write_up="""
            Converting a list of video frames into a PyTorch tensor is essential for batching and processing.
            The `ImglistToTensor` function from the `kale.prepdata.video_transform` module facilitates this conversion.
            """,
            code=load_file("code_snippets/kale_api/prepdata/video_transform.py")
        )

