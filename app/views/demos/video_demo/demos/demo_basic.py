"""
Demo 1 – Basic Sparse Sampling
Adapted from: https://github.com/pykale/pykale/tree/main/examples/video_loading

Loads 5 frames from a single video using sparse sampling
(5 segments, 1 frame each) with no transforms applied.
"""

import os
import streamlit as st
from utils.helper_utils import load_file
from views.demos.video_demo.video_backend import get_dataset
from utils.ui_utils import display_frames_in_grid
from views.components.ui import section_block, code_snippet_block

def demo_basic_sampling():
    """
    Displays a step-by-step demo of sparse frame sampling from video data.
    Uses 5 segments and 1 frame per segment (no preprocessing).
    """
    # Heading
    section_block(
        title="🍃 Basic Sampling",
        heading_level=3
    )

    # Overview section
    section_block(
        title="Overview",
        body="""
        We load <strong>5 short clips</strong> from the first video, each with 1 frame. 
        This quickly shows you different points in the video without scanning all the frames.
        """
    )

    # Implementation section
    section_block(
        title="Implementation",
        body="""
        We create a <code>VideoFrameDataset</code> with <strong>num_segments=5</strong> 
        and <strong>frames_per_segment=1</strong>. That means for each segment, we only grab 1 frame. 
        """
    )

    # Code Block Section
    code_snippet_block(
        label = "Show Code",
        code = load_file("code_snippets/video_loading/basic_sampling.py")
    )


    # Run & Display
    section_block("Results")
    
    videos_root = os.path.join(os.getcwd(), "data/demo_dataset")
    annotation_file = os.path.join(videos_root, "annotations.txt")

    dataset = get_dataset(
        root_path=videos_root,
        annotation_file=annotation_file,
        num_segments=5,
        frames_per_segment=1,
        transform=None
    )

    sample = dataset[0]
    frames = sample[0]

    display_frames_in_grid(frames, num_cols=3)
    st.markdown("---")
