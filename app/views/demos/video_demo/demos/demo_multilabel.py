"""
Demo 4 – Multi-Label Support
Adapted from: https://github.com/pykale/pykale/tree/main/examples/video_loading

Demonstrates how PyKale handles video samples with multiple labels using 
a multi-label annotation format.
"""
import os
import torch
import streamlit as st
from utils.helper_utils import load_file
from views.demos.video_demo.video_backend import get_dataset, get_preprocessor
from views.components.ui import section_block, code_snippet_block


def demo_multilabel():
    """
    Loads video clips that are annotated with multiple labels per sample.
    This demo showcases how PyKale supports multi-label datasets and how
    such annotations are structured and loaded.
    """
    section_block(
        title="👥 Multi-Label Example",
        heading_level=3
    )


    # Overview section
    section_block(
        title="Overview",
        body="""
        In some datasets, each video clip can be annotated with more than one label. 
        For example, a clip might belong to multiple classes or categories simultaneously.
        This is called <strong>multi-label classification</strong>.
        """
    )


    # Implementation section
    section_block(
        title="Implementation",
        body="""
        This dataset includes 3 labels per clip. Using 
        <code>VideoFrameDataset</code> with <em>num_segments=5</em> 
        and <em>frames_per_segment=1</em> still grabs frames, but 
        we also retrieve multiple labels for each sample.
        """
    )

    # Code Block Section
    code_snippet_block(
        label = "Show Code",
        code = load_file("code_snippets/video_loading/multi_label.py")
    )


    # Run & Display
    section_block("Results")

    videos_root = os.path.join(os.getcwd(), "datasets/demo_dataset_multilabel")
    annotation_file = os.path.join(videos_root, "annotations.txt")
    preprocess = get_preprocessor()

    dataset = get_dataset(
        root_path=videos_root,
        annotation_file=annotation_file,
        num_segments=5,
        frames_per_segment=1,
        transform=preprocess
    )

    dataloader = torch.utils.data.DataLoader(
        dataset=dataset, batch_size=3, shuffle=True, num_workers=2, pin_memory=True
    )

    for video_batch, (labels1, labels2, labels3) in dataloader:
        st.markdown(
            f"""
            <div style="text-align:center;">
              <p>Loaded a batch of <strong>{video_batch.size(0)}</strong> samples. Each sample includes <strong>3 labels</strong>.</p>
              <p style="color:#7f8c8d;">This structure is useful for tasks like action recognition, where one clip might have multiple relevant tags.</p>
              <ul style="list-style-position: inside; display:inline-block; text-align:left;">
                <li><strong>Label 1</strong>: First class or category: {labels1.size()}</li>
                <li><strong>Label 2</strong>: Second class or category: {labels2.size()}</li>
                <li><strong>Label 3</strong>: Third class or category: {labels3.size()}</li>
              </ul>
            </div>
            """,
            unsafe_allow_html=True
        )
        break
