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
    st.markdown("<h3 style='text-align: center;'>Demo 1: Basic Sampling</h3>", unsafe_allow_html=True)
    st.markdown(
        """
        <p style="text-align:center;">
        Load <strong>5 sparse segments</strong> (1 frame each) 
        from the <em>first</em> video sample in the dataset.
        </p>
        """,
        unsafe_allow_html=True
    )

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

    sample = dataset[0]
    frames = sample[0]  


    st.markdown("<h4 style='text-align:center;'>Extracted Video Frames</h4>", unsafe_allow_html=True)

    # Display frames in a grid
    display_frames_in_grid(frames, num_cols=3)


def demo_2():
    st.markdown("<h3 style='text-align: center;'>Demo 2: Continuous Frame Clip</h3>", unsafe_allow_html=True)
    st.markdown(
        """
        <p style="text-align:center;">
        Load <strong>9 consecutive frames</strong> from a single segment in the 
        <em>second</em> video sample. This illustrates continuous clip loading 
        instead of sparse sampling.
        </p>
        """,
        unsafe_allow_html=True
    )

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
    frames = sample[0]  # list of PIL images

    st.markdown("<h4 style='text-align:center;'>Extracted Video Frames</h4>", unsafe_allow_html=True)

    # Display frames in a grid
    display_frames_in_grid(frames, num_cols=3)




def demo_3():
    st.markdown("<h3 style='text-align: center;'>Demo 3: Transform & Tensor</h3>", unsafe_allow_html=True)
    st.markdown(
        """
        <p style="text-align:center;">
        Apply PyTorch transforms (<code>Resize</code>, <code>CenterCrop</code>, <code>Normalize</code>) 
        to <strong>5 sampled frames</strong> and display them. 
        Also shows a brief example of <code>DataLoader</code> usage.
        </p>
        """,
        unsafe_allow_html=True
    )

    videos_root = os.path.join(os.getcwd(), "datasets/demo_dataset")
    annotation_file = os.path.join(videos_root, "annotations.txt")

    preprocess = transforms.Compose(
        [
            ImglistToTensor(),  # list of PIL images to (FRAMES x CHANNELS x HEIGHT x WIDTH) tensor
            transforms.Resize(299),  # image batch, resize smaller edge to 299
            transforms.CenterCrop(299),  # image batch, center crop to square 299x299
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ]
    )

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

    # Show shape
    st.markdown(
        f"<h4 style='text-align:center;'>Video Tensor Size: {tuple(frame_tensor.size())}</h4>",
        unsafe_allow_html=True
    )

    # Plot Images
    frame_tensor = denormalize(frame_tensor)

    # Display frames in a grid
    st.markdown("<h4 style='text-align:center;'>Transformed & Denormalized Frames</h4>", unsafe_allow_html=True)
    display_frames_in_grid(frame_tensor, num_cols=3)


    dataloader = torch.utils.data.DataLoader(
        dataset=dataset, batch_size=2, shuffle=True, num_workers=4, pin_memory=True
    )

    st.write("---")
    st.markdown("<h4 style='text-align:center;'>DataLoader Example (first batch)</h4>", unsafe_allow_html=True)

    for video_batch, labels in dataloader:
        # Show the shape of the first batch
        st.markdown(
            f"""
            <p style="text-align:center;">
            <strong>Video Batch Tensor Size:</strong> {tuple(video_batch.size())} <br/>
            <strong>Batch Labels Shape:</strong> {tuple(labels.size())} <br/>
            Labels: {labels.tolist()}
            </p>
            """,
            unsafe_allow_html=True
        )
        break

def demo_4():
    st.markdown("<h3 style='text-align: center;'>Demo 4: Multi-Label Example</h3>", unsafe_allow_html=True)
    st.markdown(
        """
        <p style="text-align:center;">
        Demonstration of a dataset with <strong>multiple labels per sample</strong> 
        (e.g., <em>verb, noun, action</em>). We'll load the first batch from a 
        DataLoader and show how the labels are structured.
        </p>
        """,
        unsafe_allow_html=True
    )

    videos_root = os.path.join(os.getcwd(), "datasets/demo_dataset_multilabel")
    annotation_file = os.path.join(videos_root, "annotations.txt")

    preprocess = transforms.Compose(
        [
            ImglistToTensor(),  # list of PIL images to (FRAMES x CHANNELS x HEIGHT x WIDTH) tensor
            transforms.Resize(299),  # image batch, resize smaller edge to 299
            transforms.CenterCrop(299),  # image batch, center crop to square 299x299
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ]
    )

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

    dataloader = torch.utils.data.DataLoader(
        dataset=dataset, batch_size=3, shuffle=True, num_workers=2, pin_memory=True
    )

    st.markdown("<br/>", unsafe_allow_html=True)


    for video_batch, (labels1, labels2, labels3) in dataloader:
        st.markdown(
            f"""
            <div style="text-align:center;">
              <p><strong>Video Batch Tensor Size:</strong> {tuple(video_batch.size())}</p>
              <p><em>Labels1 Shape</em> (e.g., verb): {tuple(labels1.size())} — {labels1.tolist()}</p>
              <p><em>Labels2 Shape</em> (e.g., noun): {tuple(labels2.size())} — {labels2.tolist()}</p>
              <p><em>Labels3 Shape</em> (e.g., action): {tuple(labels3.size())} — {labels3.tolist()}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        break


