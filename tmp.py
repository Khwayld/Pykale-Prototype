import torch
from PIL import Image
import numpy as np
from kale.loaddata.image_access import DigitDataset
from kale.prepdata.image_transform import get_transform
from kale.embed.image_cnn import SmallCNNFeature
from kale.predict.class_domain_nets import ClassNetSmallImage
from kale.evaluate.metrics import topk_accuracy
import torchvision.transforms as T



def run_first_model_pipeline(resize=32, center_crop=28):
    """
    Runs a simple pipeline to build a digit classifier using PyKale.
    
    Steps:
    1. Load a sample image and its true digit from the MNIST dataset.
    2. Preprocess the image (resize, center crop, normalize).
    3. Extract features using a small CNN.
    4. Predict the digit with a simple classifier.
    5. Evaluate the prediction using top-1 accuracy.

    Parameters:
      - resize (int): The size to which the image is resized.
      - center_crop (int): The size for center cropping.
    
    Returns:
      - predicted_label (int): The digit predicted by the model.
      - true_label (int): The actual digit.
      - accuracy (float): Top-1 accuracy (1.0 if correct, 0.0 if incorrect).
      - preprocessed_image (numpy array): The image after preprocessing (for display).
    """
    
    try:
        # 1. Load Data
        data_path = "./datasets/digits"  # Set your desired data directory
        
        # Use the enum value (DigitDataset.MNIST) and get_access to return a dataset access object and channel info.
        data_access, num_channels = DigitDataset.get_access(DigitDataset.MNIST, data_path)
        
        # Get the training set and extract the first sample and label.
        sample, true_label = data_access.get_train()[0]

        if not isinstance(sample, Image.Image):
            if isinstance(sample, torch.Tensor):
                sample_np = sample.detach().cpu().numpy()
                
                # If image is grayscale with shape (1, H, W), squeeze channel dimension
                if sample_np.ndim == 3 and sample_np.shape[0] == 1:
                    sample_np = sample_np.squeeze(0)
                
                # Assume the tensor is in range [0,1]; multiply by 255 and convert to uint8
                sample = Image.fromarray((sample_np * 255).astype(np.uint8))
            else:
                sample = Image.fromarray(sample)


        # *** 1) Define your own transform for 3 channels ***
        transform = T.Compose([
            T.Grayscale(num_output_channels=3),  # Convert 1->3 channels
            T.Resize(resize),
            # T.CenterCrop(center_crop),        # optional if you want the crop step
            T.ToTensor(),
            T.Normalize(mean=[0.485, 0.456, 0.406],  # typical ImageNet-like stats
                        std=[0.229, 0.224, 0.225])
        ])
        preprocessed = transform(sample).unsqueeze(0)

        # *** 2) CNN & Classifier (unchanged) ***
        feature_extractor = SmallCNNFeature()  
        feature_extractor.eval()
        with torch.no_grad():
            embedding = feature_extractor(preprocessed)

        classifier = ClassNetSmallImage(input_size=128, n_class=10)
        classifier.eval()
        with torch.no_grad():
            output = classifier(embedding)
        predicted_label = output.argmax(dim=1).item()

        # Evaluate top-1 accuracy
        target_tensor = torch.tensor([true_label])
        acc_list = topk_accuracy(output, target_tensor, topk=(1,))
        accuracy = acc_list[0].item()

        # Optional: Convert for display
        inv_normalize = T.Normalize(mean=[-0.485/0.229, -0.456/0.224, -0.406/0.225],
                                    std=[1/0.229, 1/0.224, 1/0.225])
        preprocessed_image = inv_normalize(preprocessed.squeeze(0))
        preprocessed_image = (preprocessed_image * 255).byte().permute(1, 2, 0).numpy()

        return predicted_label, true_label, accuracy, preprocessed_image
    except Exception as e:
        print("Error in run_first_model_pipeline:", e)
        return None
