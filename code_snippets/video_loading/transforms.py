"""
Demo 3 – Preprocessing with Transforms
Adapted from: https://github.com/pykale/pykale/tree/main/examples/video_loading
"""

import torchvision.transforms as transforms
from kale.prepdata.video_transform import ImglistToTensor
from kale.loaddata.videos import VideoFrameDataset

# Define the preprocessing pipeline for video frames
preprocess = transforms.Compose([
    ImglistToTensor(),          # Convert list of PIL images to tensor: (Frames x Channels x Height x Width)
    transforms.Resize(299),     # Resize so that the smaller edge is 299 pixels
    transforms.CenterCrop(299), # Center crop to 299x299 dimensions
    transforms.Normalize(       # Normalize using ImageNet mean and std
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    ),
])

# Create a VideoFrameDataset instance with the preprocessing transforms
dataset = VideoFrameDataset(
    root_path=videos_root,
    annotationfile_path=annotation_file,
    num_segments=5,             # Sparse sampling: 5 segments
    frames_per_segment=1,       # 1 frame per segment
    imagefile_template="img_{:05d}.jpg",
    transform=preprocess,       # Apply the defined preprocessing pipeline
    random_shift=True,
    test_mode=False,
)

# Retrieve a sample and obtain the preprocessed video tensor
sample = dataset[1]
frame_tensor = sample[0]  # Tensor shape: (NUM_SEGMENTS * FRAMES_PER_SEGMENT x Channels x Height x Width)
label = sample[1]
