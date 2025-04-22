from kale.embed.image_cnn import SmallCNNFeature

# Initialize the CNN-based feature extractor with default parameters:
# For example, using 3 input channels (RGB images) and a kernel size of 5.
feature_extractor = SmallCNNFeature()

# Example usage:
# Assume 'preprocessed_image' is a tensor obtained after applying your preprocessing pipeline.
embedding = feature_extractor(preprocessed_image)
