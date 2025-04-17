from kale.loaddata.avmnist_datasets import AVMNISTDataset

# Example: Initialize AVMNIST dataset
avmnist_data = AVMNISTDataset()
train_loader = avmnist_data.get_train_loader()
