
import streamlit as st
from navigation import go_to

def predict_page():
    """KALE API - Model Prediction (kale.predict)"""

    # --- Page Header ---
    st.markdown(
        """
        <div style="text-align:center;">
            <h2>🔍 Model Prediction - <code>kale.predict</code></h2>
            <p style="font-size:18px;">
                This module provides tools for building models that map feature embeddings to predictions.
                It includes functions and classes for classification, regression, and other predictive tasks.
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
                The <code>kale.predict</code> module is designed to convert feature embeddings into predictions.
                It provides classes for building predictive models, enabling tasks like image classification,
                regression, and more.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("---")

    # --- Expandable Sections ---

    col1, col2, col3 = st.columns([1, 3, 1])  
    with col2:
        with st.expander("📑 ClassNetSmallImage (Image Classification)"):
            st.write(
                """
                The `ClassNetSmallImage` class is a lightweight neural network designed for image classification.
                It takes feature embeddings (produced by modules such as `kale.embed`) as input and outputs class predictions.
                Key aspects include:
                - Configurable number of output classes.
                - Integration into a larger prediction pipeline.
                """
            )
            st.code(
                """
                from kale.predict.class_domain_nets import ClassNetSmallImage

                # Initialize the classifier for a 10-class problem
                classifier = ClassNetSmallImage(num_classes=10)

                # Example usage:
                # Assume 'embedding' is obtained from an embedding module (e.g., SmallCNNFeature)
                output = classifier(embedding)
                """,
                language="python"
            )


    st.write("---")