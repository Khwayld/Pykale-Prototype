import streamlit as st
from navigation import go_to

def prepdata_page():
    """KALE API - Data Preprocessing (kale.prepdata)"""

    # --- Header Section ---
    st.markdown(
        """
        <div style="text-align:center;">
            <h2>⚙️ Data Preprocessing - <code>kale.prepdata</code></h2>
            <p style="font-size:18px;">
                This module provides functions to transform and prepare raw data for machine learning models.
                It supports image, video, and other data transformations.
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
                The <code>kale.prepdata</code> module offers essential tools for data preprocessing. Its main functionalities include:
            </p>
            <ul style="display: inline-block; text-align: left;">
                <li>🖼️ <strong>Image Transformations:</strong> Create transformation pipelines for tasks such as resizing, cropping, and normalizing images.</li>
                <li>🔄 <strong>Tensor Conversion:</strong> Convert lists of video frames into PyTorch tensors for efficient model processing.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )


    st.write("---")

    # --- Expandable Sections ---
    col1, col2, col3 = st.columns([1, 3, 1])  

    with col2:
        with st.expander("🖼️ Image Transformations"):
            st.write(
                """
                The image transformation functions in `kale.prepdata` allow you to:
                - **Resize** images to a consistent size.
                - **Crop** images to focus on important regions.
                - **Normalize** images by adjusting their pixel intensity distributions.
                One key function is `get_transform`, which creates a transformation pipeline.
                """
            )

            st.code(
                """
                from kale.prepdata.image_transform import get_transform

                # Create a transformation pipeline:
                # - Resize images to 32 pixels,
                # - Center crop to 28 pixels,
                # - Normalize pixel values.
                transform = get_transform(resize=32, center_crop=28, normalize=True)
                """
            )

    with col2:    
        with st.expander("🔄 Tensor Conversion"):
            st.write(
                """
                Converting a list of video frames into a PyTorch tensor is essential for batching and processing.
                The `ImglistToTensor` function from the `kale.prepdata.video_transform` module facilitates this conversion.
                """
            )

            st.code(
                """
                from kale.prepdata.video_transform import ImglistToTensor

                # Convert a list of image frames into a tensor.
                tensor_converter = ImglistToTensor()
                tensor = tensor_converter(image_list)
                """
            )


    st.write("---")

