
import streamlit as st
from navigation import go_to


def pipeline_page():
    """KALE API - Pipeline (kale.pipeline)"""

    # --- Page Header ---
    st.markdown(
        """
        <div style="text-align:center;">
            <h2>🔗 Machine Learning Pipelines - <code>kale.pipeline</code></h2>
            <p style="font-size:18px;">
                This module offers pre-built machine learning pipelines, facilitating tasks like neural network training, domain adaptation, and multimodal learning.
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
        <div style="text-align: center;">
            <h3>🔹 Overview</h3>
            <p>The <code>kale.pipeline</code> module provides ready-to-use machine learning pipelines, streamlining development for tasks such as:</p>
            <div style="display: inline-block; text-align: left;">
                <ul style="margin: 0; padding: 0;">
                    <li>🧠 Neural network training</li>
                    <li>🌐 Domain adaptation</li>
                    <li>🔗 Multimodal learning</li>
                </ul>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("---")

    # --- Expandable Sections ---
    col1, col2, col3 = st.columns([1, 3, 1])  
    with col2:
        with st.expander("🧠 BaseNNTrainer (Neural Network Training)"):
            st.write(
                """
                **`BaseNNTrainer`**: A foundational class for training neural network models, built upon PyTorch Lightning. 
                It standardizes essential components like:
                - Optimizer setup
                - Learning rate scheduling
                - Training, validation, and testing workflows

                This class serves as a base for specialized trainers, ensuring consistency across various neural network training tasks.
                """
            )

            st.code(
                """
                from kale.pipeline.base_nn_trainer import BaseNNTrainer

                # Initialize the trainer with desired parameters
                trainer = BaseNNTrainer(optimizer=my_optimizer, max_epochs=50, init_lr=0.001)

                # Example usage:
                # Assume 'model' is a neural network model and 'data_loader' is a data loader
                trainer.fit(model, data_loader)
                """
            )
        

        with st.expander("🌐 Domain Adaptation Trainers"):
            st.write(
                """
                The module offers trainers tailored for domain adaptation scenarios, enabling models to generalize across different data distributions:
                - **`DANNTrainer`**: Implements the Domain-Adversarial Neural Network (DANN) approach for unsupervised domain adaptation.
                - **`CDANTrainer`**: Implements the Conditional Domain-Adversarial Network (CDAN) method, enhancing DANN by conditioning the adversarial adaptation on classifier predictions.
                - **`WDGRLTrainer`**: Implements the Wasserstein Distance Guided Representation Learning (WDGRL) approach for domain adaptation.
                """
            )

            st.code(
                """
                from kale.pipeline.domain_adapter import DANNTrainer, CDANTrainer, WDGRLTrainer

                # Initialize a DANN trainer
                dann_trainer = DANNTrainer(feature_extractor=my_feature_extractor, task_classifier=my_task_classifier)

                # Initialize a CDAN trainer
                cdan_trainer = CDANTrainer(feature_extractor=my_feature_extractor, task_classifier=my_task_classifier)

                # Initialize a WDGRL trainer
                wdgrl_trainer = WDGRLTrainer(feature_extractor=my_feature_extractor, task_classifier=my_task_classifier)
                """
            )




        with st.expander("🔗 Multimodal Learning with MultimodalNNTrainer"):
            st.write(
                """
                **`MultimodalNNTrainer`**: Facilitates training neural networks that integrate multiple data modalities. 
                It manages:
                - Separate encoders for each modality
                - Fusion techniques to combine modal representations
                - A classifier head for final predictions
                This trainer streamlines the process of building and training models that leverage diverse data sources.
                """
            )

            st.code(
                """
                from kale.pipeline.base_nn_trainer import MultimodalNNTrainer

                # Initialize the multimodal trainer with modality-specific encoders and a fusion method
                trainer = MultimodalNNTrainer(encoders=[image_encoder, text_encoder], fusion_method=my_fusion_method, classifier=my_classifier)

                # Example usage:
                # Assume 'multimodal_data_loader' provides batches of multimodal data
                trainer.fit(multimodal_data_loader)
                """
            )


    st.write("---")