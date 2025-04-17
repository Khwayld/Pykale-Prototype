import streamlit as st
from utils.helper_utils import load_file

from views.components.ui import (
    info_card,
    page_header,
    button_component,
    code_snippet_block
)

def loaddata_page():
    """KALE API - Data Handling (kale.loaddata)"""
    # Header
    page_header(
        title="📂 Data Handling - <code>kale.loaddata</code>",
        subtitle="""
        This module provides standardized dataset loaders for various data modalities.
        It supports images, videos, graphs, and more, enabling seamless data integration.
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
        The <code>kale.embed</code> module provides tools for generating feature embeddings from preprocessed data.
        In many machine learning pipelines, transforming raw or preprocessed inputs into a latent feature space is a critical step.
        These embeddings can then be used by classifiers, regression models, or other downstream tasks.
        """,
        bullets=[
            "📂 <strong>DigitDataset</strong>: Standard digit datasets (MNIST, USPS, SVHN).",
            "🎵 <strong>AVMNISTDataset</strong>: Audio-visual data for multimodal tasks.",
            "🌍 <strong>MultiDomainImageFolder</strong>: For domain adaptation across multiple image domains.",
            "🎥 <strong>VideoFrameDataset</strong>: For loading and sampling video data."
        ]
    )

    # Guide section
    col1, col2, col3 = st.columns([1, 3, 1])  
    with col2:
        code_snippet_block(
            label="📂 DigitDataset (MNIST, USPS, SVHN)",
            write_up="""
            The `DigitDataset` class is used to load common digit datasets like MNIST, USPS, and SVHN.
            It handles downloading (if necessary), splitting into train/test, and providing a PyTorch DataLoader.
            Key methods include:
            - `get_access()`: Returns a DataLoader for the specified split.
            """,
            code=load_file("code_snippets/kale_api/loaddata/image_access.py")
        )

        code_snippet_block(
            label="📂🎵 AVMNISTDataset (Audio-Visual Dataset)",
            write_up="""
            The `AVMNISTDataset` class is designed for datasets that contain paired audio and visual data.
            It is particularly useful for multimodal learning tasks where synchronizing different modalities is crucial.
            Key methods include:
            - `get_train_loader()`: Retrieves a DataLoader for training data.
            - `get_test_loader()`: Retrieves a DataLoader for testing data.
            """,
            code=load_file("code_snippets/kale_api/loaddata/avmnist_datasets.py")
        )

        code_snippet_block(
            label="🌍 MultiDomainImageFolder (Domain Adaptation)",
            write_up="""
            The `MultiDomainImageFolder` class supports loading image datasets from multiple domains.
            It is especially useful in domain adaptation tasks where the source and target domains differ.
            Key features:
            - Ability to specify separate source and target domain directories.
            - Provides combined DataLoaders for training and testing.
            """,
            code=load_file("code_snippets/kale_api/loaddata/multi_domain.py")
        )

        code_snippet_block(
            label="🎥 VideoFrameDataset (Video Loading)",
            write_up="""
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
            """,
            code=load_file("code_snippets/kale_api/loaddata/videos.py")
        )