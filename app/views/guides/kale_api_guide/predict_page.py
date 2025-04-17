
import streamlit as st
from utils.helper_utils import load_file

from views.components.ui import (
    page_header,
    section_block,
    button_component,
    code_snippet_block
)

def predict_page():
    """KALE API - Model Prediction (kale.predict)"""
    # Header
    page_header(
        title="🔍 Model Prediction - <code>kale.predict</code>",
        subtitle="""
        This module provides tools for building models that map feature embeddings to predictions.
        It includes functions and classes for classification, regression, and other predictive tasks.
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
        The <code>kale.predict</code> module is designed to convert feature embeddings into predictions.
        It provides classes for building predictive models, enabling tasks like image classification,
        regression, and more.
        """,
        heading_level=3
    )
    st.write("---")


    # Guide section
    col1, col2, col3 = st.columns([1, 3, 1])  
    with col2:
        code_snippet_block(
            label="📑 ClassNetSmallImage (Image Classification)",
            write_up="""
            The `ClassNetSmallImage` class is a lightweight neural network designed for image classification.
            It takes feature embeddings (produced by modules such as `kale.embed`) as input and outputs class predictions.
            Key aspects include:
            - Configurable number of output classes.
            - Integration into a larger prediction pipeline.
            """,
            code=load_file("code_snippets/kale_api/predict/ClassNetSmallImage.py")
        )