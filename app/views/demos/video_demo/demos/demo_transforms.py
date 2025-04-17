"""
Demo 3 – Preprocessing with Transforms
Adapted from: https://github.com/pykale/pykale/tree/main/examples/video_loading

Loads video data, applies resizing, cropping, and normalization transforms,
then displays shape and visual result after denormalization.
"""

import os
import torch
import streamlit as st
from views.components.ui import section_block, code_snippet_block
from utils.helper_utils import load_file
from utils.ui_utils import display_frames_in_grid
from views.demos.video_demo.video_backend import get_dataset, get_preprocessor, denormalize


def demo_transforms():
    """
    Applies resizing, cropping, and normalization to video frames.
    """
    
    section_block(
        title="🧰 Transforms & Tensors",
        heading_level=3
    )

    # Overview section
    section_block(
        title="Overview",
        body="""
        We resize and normalize these frames, getting them ready for a neural network. 
        Then we demonstrate how a <strong>DataLoader</strong> can batch them up.
        """
    )

    # Implementation section
    section_block(
        title="Implementation",
        body="""
        A <code>transforms.Compose</code> includes <em>Resize</em>, <em>CenterCrop</em>, 
        and <em>Normalize</em>. We convert the list of frames to a PyTorch tensor, 
        so each frame is <strong>Channels x Height x Width</strong>.
        """
    )

    # Code Block Section
    code_snippet_block(
        label = "Show Code",
        code = load_file("code_snippets/video_loading/transforms.py")
    )

    # Run & Display
    section_block("Results")

    videos_root = os.path.join(os.getcwd(), "datasets/demo_dataset")
    annotation_file = os.path.join(videos_root, "annotations.txt")
    preprocess = get_preprocessor()

    dataset = get_dataset(
        root_path=videos_root,
        annotation_file=annotation_file,
        num_segments=5,
        frames_per_segment=1,
        transform=preprocess
    )

    sample = dataset[1]
    frame_tensor = sample[0]

    num_frames, channels, height, width = frame_tensor.size()

    st.markdown(
        f"""
        <div style="text-align:center;">
          <p><strong>{num_frames}</strong> frames, each with <strong>{channels}</strong> color channels, 
          at <strong>{height}×{width}</strong> resolution.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Denormalize for display
    frame_tensor = denormalize(frame_tensor)
    st.markdown("<h5 style='text-align:center;'>Transformed & Denormalized Frames</h5>", unsafe_allow_html=True)
    display_frames_in_grid(frame_tensor, num_cols=3)
    st.write("---")

    # Dataloader Preview    
    st.markdown("<h5 style='text-align:center;'>Small DataLoader Example</h5>", unsafe_allow_html=True)
    dataloader = torch.utils.data.DataLoader(dataset=dataset, batch_size=2, shuffle=True, num_workers=4, pin_memory=True)

    for video_batch, labels in dataloader:
        batch_size = video_batch.size(0)
        st.markdown(
            f"""
            <div style="text-align:center;">
              <p>We loaded a batch of <strong>{batch_size}</strong> samples at once.</p>
              <p style="color:#7f8c8d;">(For advanced users: shapes are {tuple(video_batch.size())} & {tuple(labels.size())}.)</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        break

    st.markdown("---")
