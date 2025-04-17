"""
Demo 2 – Continuous Frame Loading
Adapted from: https://github.com/pykale/pykale/tree/main/examples/video_loading
"""

from kale.loaddata.videos import VideoFrameDataset

# Create a VideoFrameDataset instance for continuous frame loading
dataset = VideoFrameDataset(
    root_path=videos_root,
    annotationfile_path=annotation_file,
    num_segments=1,         # Single segment to enforce continuity
    frames_per_segment=9,   # Load 9 consecutive frames
    imagefile_template="img_{:05d}.jpg",
    transform=None,         # No transforms applied
    random_shift=True,
    test_mode=False,
)

# Retrieve a sample (using a different index for variety)
sample = dataset[1]
frames = sample[0]  # List of 9 consecutive frames
label = sample[1]   # Video label
