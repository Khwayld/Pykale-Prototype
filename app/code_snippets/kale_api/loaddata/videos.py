from kale.loaddata.videos import VideoFrameDataset

# Example: Load video frames from a dataset
dataset = VideoFrameDataset(
    root_path="datasets/demo_dataset",
    annotationfile_path="datasets/demo_dataset/annotations.txt",
    num_segments=5,
    frames_per_segment=1,
    imagefile_template="img_{:05d}.jpg",
    transform=None,
    random_shift=True,
    test_mode=False
)

sample = dataset[0]
frames = sample[0]