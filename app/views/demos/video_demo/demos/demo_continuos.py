"""
Demo 2 – Continuous Frame Loading
Adapted from: https://github.com/pykale/pykale/tree/main/examples/video_loading

Loads 9 consecutive frames from a single segment to show motion continuity.
No transforms applied.
"""

import os
import streamlit as st
from utils.helper_utils import load_file
from views.demos.video_demo.video_backend import get_dataset
from utils.ui_utils import display_frames_in_grid
from views.components.ui import section_block, code_snippet_block

def demo_continuos():
    """
    Displays a demo of continuous frame loading using 1 segment and 9 consecutive frames.
    """
    # Heading
    section_block(
        title="🎞️ Continuous Frame Clip",
        heading_level=3
    )

    # Overview section
    section_block(
        title="Overview",
        body="""
        We load <strong>9 consecutive frames</strong> from one segment in the second video. 
        This is useful to see how the motion evolves frame by frame.
        """
    )

    # Implementation section
    section_block(
        title="Implementation",
        body="""
        By setting <strong>num_segments=1</strong> and <strong>frames_per_segment=9</strong>,
        we pull 9 continuous frames in a row, capturing a smooth slice of the video.
        """
    )

    # Code Block Section
    code_snippet_block(
        label = "Show Code",
        code = load_file("code_snippets/video_loading/continuous_frame.py")
    )


    # Run & Display
    section_block("Results")

    videos_root = os.path.join(os.getcwd(), "data/demo_dataset")
    annotation_file = os.path.join(videos_root, "annotations.txt")

    dataset = get_dataset(
        root_path=videos_root,
        annotation_file=annotation_file,
        num_segments=1,
        frames_per_segment=9,
        transform=None
    )

    sample = dataset[0]
    frames = sample[0]

    display_frames_in_grid(frames, num_cols=3)
    st.markdown("---")

