"""
Demo 4 – Multi-Label Support
Adapted from: https://github.com/pykale/pykale/tree/main/examples/video_loading
"""

import torch
from kale.loaddata.videos import VideoFrameDataset

# Create a VideoFrameDataset instance for a multi-label dataset using the same preprocessing pipeline
dataset = VideoFrameDataset(
    root_path=videos_root,
    annotationfile_path=annotation_file,
    num_segments=5,
    frames_per_segment=1,
    imagefile_template="img_{:05d}.jpg",
    transform=preprocess,  # You can use the same transform as before
    random_shift=True,
    test_mode=False,
)

# Create a DataLoader to handle batching (this example uses a batch size of 3)
dataloader = torch.utils.data.DataLoader(
    dataset=dataset,
    batch_size=3,
    shuffle=True,
    num_workers=2,
    pin_memory=True,
)

# Iterate through one batch to inspect the multi-label output
for batch in dataloader:
    video_batch, labels = batch
        
    # 'labels' is expected to be a tuple of tensors, e.g., (labels1, labels2, labels3)
    labels1, labels2, labels3 = labels
    break
