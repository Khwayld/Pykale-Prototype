from kale.predict.class_domain_nets import ClassNetSmallImage

# Initialize the classifier for a 10-class problem
classifier = ClassNetSmallImage(num_classes=10)

# Example usage:
# Assume 'embedding' is obtained from an embedding module (e.g., SmallCNNFeature)
output = classifier(embedding)
