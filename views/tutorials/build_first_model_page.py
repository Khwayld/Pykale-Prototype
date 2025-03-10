import streamlit as st
from helpers.constants import PRIMARY_COLOR
from navigation import go_to
from utils.first_model_utils import run_first_model_pipeline




def build_first_model_page():
    """
    Build Your First PyKale Model
    -----------------------------
    This page shows a simple MNIST digit classification pipeline using PyKale.
    We assume the reader already knows the basics of PyKale from:
      - 'Getting Started with PyKale' (for general overview)
      - 'The KALE API' (for deeper insights into core components)
    """

    col_left, col_mid, col_right = st.columns([1, 4, 1])


    # ----------------------------------------------------------------------------
    # 1. INTRO & PAGE HEADER
    # ----------------------------------------------------------------------------

    with col_mid:
        st.markdown(
            """
            <div style="text-align:center;">
                <h2>🚀 Build Your First PyKale Model</h2>
                <p style="font-size:18px; max-width:700px; margin:auto;">
                    Follow this quick-start guide to build and run a simple
                    digit classifier on the MNIST dataset using PyKale. <br>
                    If you’re brand-new to PyKale, consider visiting the
                    <em>Getting Started with PyKale</em> and <em>The KALE API</em>
                    pages first for more background.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        c_l, c_c, c_r = st.columns([3, 1.5, 3])
        with c_c:
            if st.button("🔙 Back to Hub"):
                go_to("hub")

        st.markdown("---")

    with col_mid:
        st.markdown(
            f"<h2 style='text-align:center; color:{PRIMARY_COLOR};'>Pipeline Overview</h2>",
            unsafe_allow_html=True
        )

        st.markdown(
            f"<h5 style='text-align:center;'>What we will do:</h5>",
            unsafe_allow_html=True
        )


        c_l, c_c, c_r = st.columns([1, 4, 0.1])
        with c_c:
            st.write(
                """
                1. **Load a single digit image** from MNIST (the popular handwritten digit dataset).
                2. **Preprocess** the image (resize, crop, normalize) for model input.
                3. **Extract features** using a simple CNN provided by PyKale.
                4. **Classify** which digit it is.
                5. **Evaluate** how accurate the prediction is.

                **Note**: The classifier here is not trained. It’s just a quick demonstration
                of how PyKale can load data and feed it through a CNN + classifier. Hence,
                the accuracy is usually random (0 or 1 if you’re testing a single sample).
                
                Check out the “How to Train the Model” section below to learn more.
                """
            )

        st.markdown("---")


    # ----------------------------------------------------------------------------
    # 2. CODE SECTIONS & EXPLANATIONS
    # ----------------------------------------------------------------------------
    
    # --- Step 1: Load Data ---
    with col_mid:
        st.markdown(
            f"<h2 style='text-align:center; color:{PRIMARY_COLOR};'>1. Load Data</h2>",
            unsafe_allow_html=True
        )

        st.write("""
            We pick an image from MNIST, which contains thousands of
            handwritten digit images (0–9). This gives us both the image and the label.
        """)

    
        with st.expander("Show How We Load the Image"):
            st.code(
                """
                from kale.loaddata.image_access import DigitDataset

                # Load the MNIST dataset (training part).
                dataset = DigitDataset(dataset_name="MNIST", train=True, download=True)
                sample, true_label = dataset[0]  # first image & label
                 """
            )

        st.markdown("---")
    
    # --- Step 2: Preprocess Data ---
    with col_mid:
        st.markdown(
            f"<h2 style='text-align:center; color:{PRIMARY_COLOR};'>2. Prepare the Image</h2>",
            unsafe_allow_html=True
        )

        col_left, col_center, col_right = st.columns([1, 4, 1])
        with col_center:
            st.write("""
                We normalize the pixel values and optionally resize/crop the image so it’s standard size for the model.
                Here, we use a special PyKale transform preset called `mnist32rgb`, 
                which:
                - Converts MNIST's 1-channel grayscale into a 3-channel image (to match the CNN’s expectations),
                - Resizes the image to 32×32,
                - Normalizes using ImageNet-like statistics.
            """)

    
        with st.expander("Show Preprocessing Code"):
            st.code(
                """
                from kale.prepdata.image_transform import get_transform

                transform = get_transform("mnist32rgb", augment=False)
                preprocessed = transform(sample).unsqueeze(0)  # add batch dimension
                """
            )

        st.markdown("---")
    
    # --- Step 3: Extract Features ---
    with col_mid:
        st.markdown(
            f"<h2 style='text-align:center; color:{PRIMARY_COLOR};'>3. Extract Important Features</h2>",
            unsafe_allow_html=True
        )

        st.write(
            """
            PyKale’s `SmallCNNFeature` is a mini CNN that turns our preprocessed
            image into a vector of features. Think of it as a “feature encoder”:
            it learns shapes and patterns for classification.
            """
        )
    

        with st.expander("Show Feature Extraction Code"):
            st.code(
                """
                from kale.embed.image_cnn import SmallCNNFeature
                import torch

                feature_extractor = SmallCNNFeature()
                feature_extractor.eval()
                with torch.no_grad():
                    embedding = feature_extractor(preprocessed)
                """,
            )

        st.markdown("---")



    # --- Step 4: Predict the Digit ---
    with col_mid:
        st.markdown(
            f"<h2 style='text-align:center; color:{PRIMARY_COLOR};'>4. Predict the Digit</h2>",
            unsafe_allow_html=True
        )

        st.write(
            """
            We feed the extracted features into `ClassNetSmallImage`, a simple classification head
            for 10 possible digits (0–9). Since we’re not training, it’s mostly guessing at this point.
            """
        )
    

        with st.expander("Show Prediction Code"):
            st.code(
                """
                from kale.predict.class_domain_nets import ClassNetSmallImage

                classifier = ClassNetSmallImage(input_size=128, n_class=10)
                classifier.eval()
                with torch.no_grad():
                    output = classifier(embedding)
                predicted_label = output.argmax(dim=1).item()
                """,
            )

        st.markdown("---")

    
    # --- Step 5: Evaluate the Prediction ---
    with col_mid:
        st.markdown(
            f"<h2 style='text-align:center; color:{PRIMARY_COLOR};'>5. Check the Result</h2>",
            unsafe_allow_html=True
        )

        st.write(
            """
            We compare our model’s predicted label to the true label using `topk_accuracy`.
            Because we’re only testing on **one** sample, accuracy is always 0 or 1.
            """
        )
    

        with st.expander("Show Evaluation Code"):
            st.code(
                """
                from kale.evaluate.metrics import topk_accuracy
                import torch

                target_tensor = torch.tensor([true_label])
                acc_list = topk_accuracy(output, target_tensor, topk=(1,))
                accuracy = acc_list[0].item()  # 0.0 or 1.0
                """,
            )

        st.markdown("---")


    # --------------------------------------------------------------------
    # 3) INTERACTIVE DEMO
    # --------------------------------------------------------------------

    with col_mid:
        st.markdown(
            f"""
            <div style="text-align:center;">
                <h2 style='text-align:center; color:{PRIMARY_COLOR};'>Interactive Demo: Run the Pipeline</h2>
                <p>
                    Click the button below to run the pipeline on a random MNIST sample.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        _, c_c1, _ = st.columns([3.3, 2, 3.3])

        with c_c1:
            if st.button("Run Model Pipeline"):
                with st.spinner("Running the pipeline..."):
                    result = run_first_model_pipeline() 
                if result is None:
                    st.error("An error occurred. Please try again.")
                else:
                    predicted_label, true_label, accuracy, preprocessed_image = result
                    st.markdown(f"**Predicted Digit:** {predicted_label}")
                    st.markdown(f"**True Digit:** {true_label}")
                    st.markdown(f"**Accuracy:** {accuracy:.2f}")
                    st.image(preprocessed_image, caption="Preprocessed Image")

        st.markdown("---")

    # --------------------------------------------------------------------
    # 4) HOW TO TRAIN THE MODEL
    # --------------------------------------------------------------------
    with col_mid:
        st.markdown(
            f"<h2 style='text-align:center; color:{PRIMARY_COLOR};'>How to Train the Model</h2>",
            unsafe_allow_html=True
        )

        st.write(
            """
            Since the CNN and classifier are **untrained**, their predictions are basically random.
            Below are two common ways to achieve meaningful accuracy:
            """
        )

        # Option A: Train from scratch
        with st.expander("Option A: Train from scratch (Detailed Steps)"):
            st.write(
                """
                """
            )

            st.code(
                """
                """
            )

            st.write(
                """
                After training, you can insert your trained `feature_extractor` and `classifier`
                into this demo pipeline. Then you’ll see much better (and more consistent!) predictions.
                """
            )

        # Option B: Load a Pretrained Model
        with st.expander("Option B: Load a Pretrained Model"):
            st.write(
                """
                """
            )

            st.code(
                """
                """
            )

            st.write(
                """
                With these pretrained weights in place, your pipeline should yield accurate predictions 
                on each MNIST sample. 
                """
            )

        
        st.markdown("---")


    # --------------------------------------------------------------------
    # 5) Summary
    # --------------------------------------------------------------------
    with col_mid:
        st.markdown(
            f"<h2 style='text-align:center; color:{PRIMARY_COLOR};'>Summary & Next Steps</h2>",
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div style="text-align: center; max-width: 700px; margin:auto;">
                <p style="margin-top: 10px;">
                    That’s it! You’ve built a simple digit classifier in PyKale.            
                    <strong>Feel free to experiment</strong> with different transformations or deeper neural architectures.
                </p>
            </div>
            """, 
            unsafe_allow_html=True
        )


        st.markdown("---")
