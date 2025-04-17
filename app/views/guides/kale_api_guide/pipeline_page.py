import streamlit as st
from utils.helper_utils import load_file

from views.components.ui import (
    info_card,
    page_header,
    button_component,
    code_snippet_block
)

def pipeline_page():
    """KALE API - Pipeline (kale.pipeline)"""
    # Header
    page_header(
        title="🔗 Machine Learning Pipelines - <code>kale.pipeline</code>",
        subtitle="""
        This module offers pre-built machine learning pipelines, facilitating tasks 
        like neural network training, domain adaptation, and multimodal learning.        
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
        The <code>kale.pipeline</code> module provides ready-to-use machine learning pipelines, 
        streamlining development for tasks such as:        
        """,
        bullets=[
            "🧠 Neural network training",
            "🌐 Domain adaptation",
            "🔗 Multimodal learning",
        ]
    )

    # Guide section
    col1, col2, col3 = st.columns([1, 3, 1])  
    with col2:
        code_snippet_block(
            label="🧠 BaseNNTrainer (Neural Network Training)",
            write_up="""
            **`BaseNNTrainer`**: A foundational class for training neural network models, built upon PyTorch Lightning. 
            It standardizes essential components like:
            - Optimizer setup
            - Learning rate scheduling
            - Training, validation, and testing workflows

            This class serves as a base for specialized trainers, ensuring consistency across various neural network training tasks.
            """,
            code=load_file("code_snippets/kale_api/pipeline/BaseNNTrainer.py")
        )

        code_snippet_block(
            label="🌐 Domain Adaptation Trainers",
            write_up="""
            The module offers trainers tailored for domain adaptation scenarios, enabling models to generalize across different data distributions:
            - **`DANNTrainer`**: Implements the Domain-Adversarial Neural Network (DANN) approach for unsupervised domain adaptation.
            - **`CDANTrainer`**: Implements the Conditional Domain-Adversarial Network (CDAN) method, enhancing DANN by conditioning the adversarial adaptation on classifier predictions.
            - **`WDGRLTrainer`**: Implements the Wasserstein Distance Guided Representation Learning (WDGRL) approach for domain adaptation.
            """,
            code=load_file("code_snippets/kale_api/pipeline/domain_adapter.py")
        )

        code_snippet_block(
            label="🔗 Multimodal Learning with MultimodalNNTrainer",
            write_up="""
            **`MultimodalNNTrainer`**: Facilitates training neural networks that integrate multiple data modalities. 
            It manages:
            - Separate encoders for each modality
            - Fusion techniques to combine modal representations
            - A classifier head for final predictions
            This trainer streamlines the process of building and training models that leverage diverse data sources.
            """,
            code=load_file("code_snippets/kale_api/pipeline/MultimodalNNTrainer.py")
        )