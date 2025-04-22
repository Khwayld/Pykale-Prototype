"""
Demo 1 – Basic Sparse Sampling
Adapted from: https://github.com/pykale/pykale/tree/main/examples/video_loading
"""

from kale.loaddata.videos import VideoFrameDataset

# Create a VideoFrameDataset instance without applying any transforms
dataset = VideoFrameDataset(
    root_path=videos_root,                # Path to your video frames directory
    annotationfile_path=annotation_file,   # Path to the annotations file
    num_segments=5,                        # Divide each video into 5 segments
    frames_per_segment=1,                  # Extract 1 frame per segment (sparse sampling)
    imagefile_template="img_{:05d}.jpg",
    transform=None,                        # No preprocessing transforms
    random_shift=True,
    test_mode=False,
)
    
# Retrieve the first video sample
sample = dataset[0]
frames = sample[0]  # List of PIL images
label = sample[1]   # Video label (integer)
