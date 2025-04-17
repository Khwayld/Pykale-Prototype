"""
Adapted from PyKale's toy domain adaptation demo:
https://github.com/pykale/pykale/tree/main/examples/toy_domain_adaptation

Author: Shuo Zhou
"""

# We import 'make_blobs' for creating synthetic datasets.
from sklearn.datasets import make_blobs
import numpy as np
    
# For demonstration, we fix N_SAMPLES to 200 
N_SAMPLES = 200

# Optionally set a random seed for reproducibility
np.random.seed(42)

# Create source dataset
xs, ys = make_blobs(
    n_samples=N_SAMPLES, 
    centers=[[0, 0], [0, 2]], 
    cluster_std=[0.3, 0.35]
)

# Create target dataset
xt, yt = make_blobs(
    n_samples=N_SAMPLES, 
    centers=[[2, -2], [2, 0.2]], 
    cluster_std=[0.35, 0.4]
)
