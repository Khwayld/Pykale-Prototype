import streamlit as st
from utils.helper_utils import load_file

from views.components.ui import (
    page_header,
    section_block,
    button_component,
    code_snippet_block
)

def embed_page():
    """KALE API - Feature Extraction & Embedding (kale.embed)"""

    # Header
    page_header(
        title="📑 Feature Extraction & Embedding - <code>kale.embed</code>",
        subtitle="""
        This module provides functions to convert preprocessed data into meaningful feature representations.
        These embeddings serve as the input to subsequent prediction tasks.
        """
    )
    
    button_component(
        button_text="🔙 Back to API Guide",
        slug="kale_api"
    )
    

    # Overview
    section_block(
        title="🔹 Overview",
        body="""
        The <code>kale.embed</code> module provides tools for generating feature embeddings from preprocessed data.
        In many machine learning pipelines, transforming raw or preprocessed inputs into a latent feature space is a critical step.
        These embeddings can then be used by classifiers, regression models, or other downstream tasks.
        """,
        heading_level=2
    )
    st.write("---")


    # Guide section
    col1, col2, col3 = st.columns([1, 3, 1])  
    with col2:
        code_snippet_block(
            label="📌 SmallCNNFeature (CNN-based Embedding for Images)",
            write_up="""
            The `SmallCNNFeature` class is a lightweight convolutional neural network designed for small 32x32 images (e.g. CIFAR, MNIST) 
            that outputs a feature vector of length 128.

            It is particularly useful when you need a fast and efficient embedding method for small or simple image datasets.

            Key characteristics:
            - Processes input images into a lower-dimensional representation.
            - Can be used as the encoder in a larger pipeline.

            **Parameters:**
            - `num_channels (int):` The number of input channels (default=3).
            - `kernel_size (int):` The size of the convolution kernel (default=5).
            """,
            code=load_file("code_snippets/kale_api/embed/smallcnn.py")
        )