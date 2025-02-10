import os

import matplotlib.pyplot as plt
import torch
from mpl_toolkits.axes_grid1 import ImageGrid
from torchvision import transforms

from kale.loaddata.videos import VideoFrameDataset
from kale.prepdata.video_transform import ImglistToTensor
import streamlit as st


def denormalize(video_tensor):
    """
    Undoes mean/standard deviation normalization, zero to one scaling,
    and channel rearrangement for a batch of images.
    args:
        video_tensor: a (FRAMES x CHANNELS x HEIGHT x WIDTH) tensor
    """
    inverse_normalize = transforms.Normalize(
        mean=[-0.485 / 0.229, -0.456 / 0.224, -0.406 / 0.225], std=[1 / 0.229, 1 / 0.224, 1 / 0.225]
    )
    return (inverse_normalize(video_tensor) * 255.0).type(torch.uint8).permute(0, 2, 3, 1).numpy()

def display_frames_in_grid(frames, num_cols=3):
    """
    Helper function to display a list of frames (PIL images or arrays) in a grid layout.
    Each row has `num_cols` columns.
    """
    rows_needed = (len(frames) + num_cols - 1) // num_cols
    for row_idx in range(rows_needed):
        cols = st.columns(num_cols)
        for col_idx in range(num_cols):
            frame_index = row_idx * num_cols + col_idx
            if frame_index < len(frames):
                with cols[col_idx]:
                    st.markdown(
                        f"<h5 style='text-align: center;'>Frame {frame_index + 1}</h5>",
                        unsafe_allow_html=True
                    )
                    st.image(frames[frame_index], use_column_width=True)



def demo_1():
    # Main heading for the demo
    st.markdown(
        "<h3 style='text-align: center; color:#16a085;'>🍃 Basic Sampling</h3>",
        unsafe_allow_html=True
    )

    # 1. Overview
    st.markdown("<h4 style='text-align:center; color:#16a085;'>Overview</h4>", unsafe_allow_html=True)
    st.markdown("""
    <p style="text-align:center;">
      We load <strong>5 short clips</strong> from the first video, each with 1 frame. 
      This quickly shows you different points in the video without scanning all the frames.
    </p>
    """, unsafe_allow_html=True)

    # 2. Implementation
    st.markdown("<h4 style='text-align:center; color:#16a085;'>Implementation</h4>", unsafe_allow_html=True)
    st.markdown("""
    <p style="text-align:center;">
      We create a <code>VideoFrameDataset</code> with <strong>num_segments=5</strong> 
      and <strong>frames_per_segment=1</strong>. That means for each segment, we only grab 1 frame. 
    </p>
    """, unsafe_allow_html=True)
    # (No large code snippet here; or you could put st.code(...) if you want.)

    # 3. Results
    st.markdown("<h4 style='text-align:center; color:#16a085;'>Results</h4>", unsafe_allow_html=True)

    videos_root = os.path.join(os.getcwd(), "datasets/demo_dataset")
    annotation_file = os.path.join(videos_root, "annotations.txt")

    dataset = VideoFrameDataset(
        root_path=videos_root,
        annotationfile_path=annotation_file,
        num_segments=5,
        frames_per_segment=1,
        imagefile_template="img_{:05d}.jpg",
        transform=None,
        random_shift=True,
        test_mode=False,
    )

    # Grab the first sample
    sample = dataset[0]
    frames = sample[0]

    display_frames_in_grid(frames, num_cols=3)

def demo_2():
    # Main heading
    st.markdown(
        "<h3 style='text-align: center; color:#16a085;'>🎞️ Continuous Frame Clip</h3>",
        unsafe_allow_html=True
    )

    # 1. Overview
    st.markdown("<h4 style='text-align:center; color:#16a085;'>Overview</h4>", unsafe_allow_html=True)
    st.markdown("""
    <p style="text-align:center;">
      We load <strong>9 consecutive frames</strong> from one segment in the second video. 
      This is useful to see how the motion evolves frame by frame.
    </p>
    """, unsafe_allow_html=True)

    # 2. Implementation
    st.markdown("<h4 style='text-align:center; color:#16a085;'>Implementation</h4>", unsafe_allow_html=True)
    st.markdown("""
    <p style="text-align:center;">
      By setting <strong>num_segments=1</strong> and <strong>frames_per_segment=9</strong>,
      we pull 9 continuous frames in a row, capturing a smooth slice of the video.
    </p>
    """, unsafe_allow_html=True)

    # 3. Results
    st.markdown("<h4 style='text-align:center; color:#16a085;'>Results</h4>", unsafe_allow_html=True)

    videos_root = os.path.join(os.getcwd(), "datasets/demo_dataset")
    annotation_file = os.path.join(videos_root, "annotations.txt")

    dataset = VideoFrameDataset(
        root_path=videos_root,
        annotationfile_path=annotation_file,
        num_segments=1,
        frames_per_segment=9,
        imagefile_template="img_{:05d}.jpg",
        transform=None,
        random_shift=True,
        test_mode=False,
    )

    sample = dataset[1]
    frames = sample[0]

    display_frames_in_grid(frames, num_cols=3)




def demo_3():
    st.markdown(
        "<h3 style='text-align: center; color:#16a085;'>🧰 Transforms & Tensors</h3>",
        unsafe_allow_html=True
    )

    # 1. Overview
    st.markdown("<h4 style='text-align:center; color:#16a085;'>Overview</h4>", unsafe_allow_html=True)
    st.markdown("""
    <p style="text-align:center;">
      We resize and normalize these frames, getting them ready for a neural network. 
      Then we demonstrate how a <strong>DataLoader</strong> can batch them up.
    </p>
    """, unsafe_allow_html=True)

    # 2. Implementation
    st.markdown("<h4 style='text-align:center; color:#16a085;'>Implementation</h4>", unsafe_allow_html=True)
    st.markdown("""
    <p style="text-align:center;">
      A <code>transforms.Compose</code> includes <em>Resize</em>, <em>CenterCrop</em>, 
      and <em>Normalize</em>. We convert the list of frames to a PyTorch tensor, 
      so each frame is <strong>Channels × Height × Width</strong>.
    </p>
    """, unsafe_allow_html=True)

    videos_root = os.path.join(os.getcwd(), "datasets/demo_dataset")
    annotation_file = os.path.join(videos_root, "annotations.txt")

    preprocess = transforms.Compose([
        ImglistToTensor(),
        transforms.Resize(299),
        transforms.CenterCrop(299),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

    dataset = VideoFrameDataset(
        root_path=videos_root,
        annotationfile_path=annotation_file,
        num_segments=5,
        frames_per_segment=1,
        imagefile_template="img_{:05d}.jpg",
        transform=preprocess,
        random_shift=True,
        test_mode=False,
    )

    sample = dataset[1]
    frame_tensor = sample[0]

    # 3. Results
    st.markdown("<h4 style='text-align:center; color:#16a085;'>Results</h4>", unsafe_allow_html=True)

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

def demo_4():
    st.markdown(
        "<h3 style='text-align: center; color:#16a085;'>👥 Multi-Label Example</h3>",
        unsafe_allow_html=True
    )

    # 1. Overview
    st.markdown("<h4 style='text-align:center; color:#16a085;'>Overview</h4>", unsafe_allow_html=True)
    st.markdown("""
    <p style="text-align:center;">
      Some video clips have <strong>multiple labels</strong> (e.g., verb, noun, action). 
      We load a small batch to see how that works in practice.
    </p>
    """, unsafe_allow_html=True)

    # 2. Implementation
    st.markdown("<h4 style='text-align:center; color:#16a085;'>Implementation</h4>", unsafe_allow_html=True)
    st.markdown("""
    <p style="text-align:center;">
      This dataset includes 3 labels per clip. Using 
      <code>VideoFrameDataset</code> with <em>num_segments=5</em> 
      and <em>frames_per_segment=1</em> still grabs frames, but 
      we also retrieve multiple labels for each sample.
    </p>
    """, unsafe_allow_html=True)

    videos_root = os.path.join(os.getcwd(), "datasets/demo_dataset_multilabel")
    annotation_file = os.path.join(videos_root, "annotations.txt")

    preprocess = transforms.Compose([
        ImglistToTensor(),
        transforms.Resize(299),
        transforms.CenterCrop(299),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

    dataset = VideoFrameDataset(
        root_path=videos_root,
        annotationfile_path=annotation_file,
        num_segments=5,
        frames_per_segment=1,
        imagefile_template="img_{:05d}.jpg",
        transform=preprocess,
        random_shift=True,
        test_mode=False,
    )

    # 3. Results
    st.markdown("<h4 style='text-align:center; color:#16a085;'>Results</h4>", unsafe_allow_html=True)

    dataloader = torch.utils.data.DataLoader(
        dataset=dataset, batch_size=3, shuffle=True, num_workers=2, pin_memory=True
    )

    for video_batch, (labels1, labels2, labels3) in dataloader:
        batch_size = video_batch.size(0)
        st.markdown(
            f"""
            <div style="text-align:center;">
              <p>We loaded <strong>{batch_size}</strong> samples. Each has 3 labels 
                (<em>verb, noun, action</em> or similar).</p>
              <p style="color:#7f8c8d;">For instance:</p>
              <ul style="list-style-position: inside; display:inline-block; text-align:left;">
                <li><strong>Labels1</strong> could be a verb (run, jump, etc.)</li>
                <li><strong>Labels2</strong> could be a noun (ball, table, etc.)</li>
                <li><strong>Labels3</strong> could be the combined action (e.g., “run with ball”).</li>
              </ul>
            </div>
            """,
            unsafe_allow_html=True
        )
        break


