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


def demo_1():
    videos_root = os.path.join(os.getcwd(), "demo_dataset")
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


    # Plot Images
    for index in range(len(frames)):
        st.title(index)
        st.image(frames[index])



def demo_2():
    videos_root = os.path.join(os.getcwd(), "demo_dataset")
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

    # Plot Images
    for index in range(len(frames)):
        st.title(index)
        st.image(frames[index])




def demo_3():
    videos_root = os.path.join(os.getcwd(), "demo_dataset")
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
    frames = sample[0]  
    frame_tensor = sample[0]  

    st.subheader(f"Video Tensor Size: {str(frame_tensor.size())}")

    # Plot Images
    frame_tensor = denormalize(frame_tensor)

    for index in range(len(frame_tensor)):
        st.title(index)
        st.image(frame_tensor[index])


    dataloader = torch.utils.data.DataLoader(
        dataset=dataset, batch_size=2, shuffle=True, num_workers=4, pin_memory=True
    )

    for epoch in range(10):
        for video_batch, labels in dataloader:
            """
            Insert Training Code Here
            """

            st.subheader(labels)
            st.subheader(f"Video Batch Tensor Size: {str(video_batch.size())}")
            st.subheader(f"Batch Labels Size: {str(labels.size())}")
            break
        break

def demo_4():
    videos_root = os.path.join(os.getcwd(), "demo_dataset_multilabel")
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

    st.title("\nMulti-Label Example")
    for epoch in range(10):
        for batch in dataloader:
            """
            Insert Training Code Here
            """
            video_batch, (labels1, labels2, labels3) = batch

            st.subheader(f"Video Batch Tensor Size: {str(video_batch.size())}")
            st.subheader(f"Labels1 Size: {str(labels1.size())}") 
            st.subheader(f"Labels2 Size:{str(labels2.size())}")  
            st.subheader(f"Labels3 Size: {str(labels3.size())}")  
            break
        break


