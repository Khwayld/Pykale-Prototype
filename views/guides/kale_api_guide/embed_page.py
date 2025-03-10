import streamlit as st
from navigation import go_to

def embed_page():
    """KALE API - Feature Extraction & Embedding (kale.embed)"""

    # --- Page Header ---
    st.markdown(
        """
        <div style="text-align:center;">
            <h2>📑 Feature Extraction & Embedding - <code>kale.embed</code></h2>
            <p style="font-size:18px;">
                This module provides functions to convert preprocessed data into meaningful feature representations.
                These embeddings serve as the input to subsequent prediction tasks.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    col_left, col_center, col_right = st.columns([3, 1, 3])
    with col_center:
        if st.button("🔙 Back to API Guide"):
            go_to("kale_api")

    st.write("---")

    # --- Overview Section ---
    st.markdown(
        """
        <div style="text-align:center;">
            <h3>🔹 Overview</h3>
            <p>
                The <code>kale.embed</code> module provides tools for generating feature embeddings from preprocessed data.
                In many machine learning pipelines, transforming raw or preprocessed inputs into a latent feature space is a critical step.
                These embeddings can then be used by classifiers, regression models, or other downstream tasks.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("---")

    # --- Expandable Sections ---
    col1, col2, col3 = st.columns([1, 3, 1])  
    with col2:
        with st.expander("📌 SmallCNNFeature (CNN-based Embedding for Images)"):
            st.write(
                """
                The `SmallCNNFeature` class is a lightweight convolutional neural network designed for small 32x32 images (e.g. CIFAR, MNIST) 
                that outputs a feature vector of length 128.

                It is particularly useful when you need a fast and efficient embedding method for small or simple image datasets.

                Key characteristics:
                - Processes input images into a lower-dimensional representation.
                - Can be used as the encoder in a larger pipeline.

                **Parameters:**
                - `num_channels (int):` The number of input channels (default=3).
                - `kernel_size (int):` The size of the convolution kernel (default=5).
                """
            )

            st.code(
                """
                from kale.embed.image_cnn import SmallCNNFeature

                # Initialize the CNN-based feature extractor with default parameters:
                # For example, using 3 input channels (RGB images) and a kernel size of 5.
                feature_extractor = SmallCNNFeature()

                # Example usage:
                # Assume 'preprocessed_image' is a tensor obtained after applying your preprocessing pipeline.
                embedding = feature_extractor(preprocessed_image)
                """
            )

    st.write("---")