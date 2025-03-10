import streamlit as st
from navigation import go_to

def loaddata_page():
    """KALE API - Data Handling (kale.loaddata)"""

    # --- Page Header ---
    st.markdown(
        """
        <div style="text-align:center;">
            <h2>📂 Data Handling - <code>kale.loaddata</code></h2>
            <p style="font-size:18px;">
                This module provides standardized dataset loaders for various data modalities.
                It supports images, videos, graphs, and more, enabling seamless data integration.
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
            <p>The <code>kale.loaddata</code> module is designed to load and preprocess datasets. 
            It includes several specialized classes, such as:</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown(
        """
        <div style="text-align:center;">
            <ul style="display: inline-block; text-align: left;">
                <li>📂 <strong>DigitDataset</strong>: Standard digit datasets (MNIST, USPS, SVHN).</li>
                <li>🎵 <strong>AVMNISTDataset</strong>: Audio-visual data for multimodal tasks.</li>
                <li>🌍 <strong>MultiDomainImageFolder</strong>: For domain adaptation across multiple image domains.</li>
                <li>🎥 <strong>VideoFrameDataset</strong>: For loading and sampling video data.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("---")

    # --- Expandable Sections ---

    # 1. DigitDataset
    col1, col2, col3 = st.columns([1, 3, 1])  
    with col2:
        with st.expander("📂 DigitDataset (MNIST, USPS, SVHN)"):
            st.write(
                """
                The `DigitDataset` class is used to load common digit datasets like MNIST, USPS, and SVHN.
                It handles downloading (if necessary), splitting into train/test, and providing a PyTorch DataLoader.
                Key methods include:
                - `get_access()`: Returns a DataLoader for the specified split.
                """
            )
            st.code(
                """
                from kale.loaddata.image_access import DigitDataset

                # Example: Load the MNIST dataset
                dataset = DigitDataset(dataset_name="MNIST", train=True, download=True)
                train_loader = dataset.get_access()
                """
            )

    # 2. AVMNISTDataset
    with col2:
        with st.expander("🎵 AVMNISTDataset (Audio-Visual Dataset)"):
            st.write(
                """
                The `AVMNISTDataset` class is designed for datasets that contain paired audio and visual data.
                It is particularly useful for multimodal learning tasks where synchronizing different modalities is crucial.
                Key methods include:
                - `get_train_loader()`: Retrieves a DataLoader for training data.
                - `get_test_loader()`: Retrieves a DataLoader for testing data.
                """
            )
            st.code(
                """
                from kale.loaddata.avmnist_datasets import AVMNISTDataset

                # Example: Initialize AVMNIST dataset
                avmnist_data = AVMNISTDataset()
                train_loader = avmnist_data.get_train_loader()
                """
            )

    # 3. MultiDomainImageFolder
    with col2:
        with st.expander("🌍 MultiDomainImageFolder (Domain Adaptation)"):
            st.write(
                """
                The `MultiDomainImageFolder` class supports loading image datasets from multiple domains.
                It is especially useful in domain adaptation tasks where the source and target domains differ.
                Key features:
                - Ability to specify separate source and target domain directories.
                - Provides combined DataLoaders for training and testing.
                """
            )
            st.code(
                """
                from kale.loaddata.multi_domain import MultiDomainImageFolder

                # Example: Initialize MultiDomainImageFolder with source and target paths
                multi_domain_data = MultiDomainImageFolder(
                    source_domains=["/path/to/source"],
                    target_domains=["/path/to/target"]
                )
                train_loader = multi_domain_data.get_train()
                """
            )

    # 4. VideoFrameDataset
    with col2:
        with st.expander("🎥 VideoFrameDataset (Video Loading)"):
            st.write(
                """
                The `VideoFrameDataset` class makes it easy to load video data by extracting only a few key frames from each video.
                Instead of loading every frame, it selects a few representative frames to capture the action across the entire video.

                **Parameters Explained:**
                - `root_path`: The main folder where your video folders are stored.
                - `annotationfile_path`: A text file listing each video sample along with the frame range and its label.
                - `num_segments`: The video is divided into this many parts; a frame is selected from each segment.
                - `frames_per_segment`: The number of consecutive frames to load from each segment.
                - `imagefile_template`: The naming pattern for the video frame files (e.g., "img_00001.jpg").
                - `transform`: An optional processing step for the images (set to None if not needed).
                - `random_shift`: If True, the starting frame in each segment is chosen randomly; if False, it uses the middle frame.
                - `test_mode`: If True, frames are chosen in a fixed manner for testing; if False, random selection is used.

                """
            )
            
            st.code(
                """
                from kale.loaddata.videos import VideoFrameDataset

                # Example: Load video frames from a dataset
                dataset = VideoFrameDataset(
                    root_path="datasets/demo_dataset",
                    annotationfile_path="datasets/demo_dataset/annotations.txt",
                    num_segments=5,
                    frames_per_segment=1,
                    imagefile_template="img_{:05d}.jpg",
                    transform=None,
                    random_shift=True,
                    test_mode=False
                )

                sample = dataset[0]
                frames = sample[0]
                """
            )

    st.write("---")