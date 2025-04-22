from kale.prepdata.image_transform import get_transform

# Create a transformation pipeline:
# - Resize images to 32 pixels,
# - Center crop to 28 pixels,
# - Normalize pixel values.
transform = get_transform(resize=32, center_crop=28, normalize=True)