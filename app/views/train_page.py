import streamlit as st
from ml_core.train import train_model
from ml_core.registry import ModelRegistry


def train_model_page():
    """
    """
    col_left, col_center, col_right = st.columns([1,4,1])
    with col_center:
        st.title("No-Code Model Trainer")

        model_choice = st.selectbox("Select Model", ModelRegistry.list_models())
        
        if model_choice is not None:
            Model = ModelRegistry.get(model_choice)
            dataset_choice = st.selectbox("Select Dataset", Model.supported_datasets())
            
            ckpt = None

            action = st.radio(
                "Select choice:",
                ("Train New Model", "Upload Existing Model")
            )

            if action == "Train New Model":
                epochs = st.slider("Epochs", min_value=1, max_value=10, value=3)

                if st.button("Start Training"):
                    ckpt = train_model(model_choice, epochs)
                    st.success(f"Checkpoint: {ckpt}")
            else:
                ckpt = st.file_uploader("Upload a .ckpt file", type="ckpt")

            if ckpt is not None:
                Model.render_ui(ckpt)