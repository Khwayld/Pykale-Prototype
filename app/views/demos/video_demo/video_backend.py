"""
Adapted from PyKale's video loading demo:
https://github.com/pykale/pykale/tree/main/examples/toy_domain_adaptation

Author: Ravio Koot
"""

import torch
from torchvision import transforms
from kale.loaddata.videos import VideoFrameDataset
from kale.prepdata.video_transform import ImglistToTensor


def denormalize(video_tensor):
    """
    Undoes mean/standard deviation normalization, zero to one scaling,
    and channel rearrangement for a batch of images.
    
    Args:
        video_tensor: a (FRAMES x CHANNELS x HEIGHT x WIDTH) tensor
    """
    inverse_normalize = transforms.Normalize(
        mean=[-0.485 / 0.229, -0.456 / 0.224, -0.406 / 0.225], std=[1 / 0.229, 1 / 0.224, 1 / 0.225]
    )
    return (inverse_normalize(video_tensor) * 255.0).type(torch.uint8).permute(0, 2, 3, 1).numpy()



def get_dataset(
    root_path,
    annotation_file,
    num_segments=5,
    frames_per_segment=1,
    transform=None
):
    """
    Creates a PyKale VideoFrameDataset instance.

    Args:
        root_path: Path to dataset root directory.
        annotation_file: Path to annotation file.
        num_segments: Number of temporal segments to sample.
        frames_per_segment: Frames per segment.
        transform: Optional transform pipeline.

    Returns:
        VideoFrameDataset: Initialized dataset
    """
    return VideoFrameDataset(
        root_path=root_path,
        annotationfile_path=annotation_file,
        num_segments=num_segments,
        frames_per_segment=frames_per_segment,
        imagefile_template="img_{:05d}.jpg",
        transform=transform,
        random_shift=True,
        test_mode=False,
    )


def get_preprocessor(image_size=299):
    """
    Returns a preprocessing pipeline for video frames.

    Includes:
    - Convert list of PIL images to tensor
    - Resize
    - Center crop
    - Normalize

    Args:
        image_size: Final height/width after crop

    Returns:
        torchvision.transforms.Compose: Transform pipeline
    """
    return transforms.Compose([
        ImglistToTensor(),
        transforms.Resize(image_size),
        transforms.CenterCrop(image_size),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )
    ])

