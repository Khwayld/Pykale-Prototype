from kale.prepdata.video_transform import ImglistToTensor

# Convert a list of image frames into a tensor.
tensor_converter = ImglistToTensor()
tensor = tensor_converter(image_list)