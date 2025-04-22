from kale.loaddata.image_access import DigitDataset

# Example: Load the MNIST dataset
dataset = DigitDataset(dataset_name="MNIST", train=True, download=True)
train_loader = dataset.get_access()
