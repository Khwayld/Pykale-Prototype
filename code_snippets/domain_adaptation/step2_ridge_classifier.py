"""
Adapted from PyKale's toy domain adaptation demo:
https://github.com/pykale/pykale/tree/main/examples/toy_domain_adaptation

Author: Shuo Zhou
"""

import numpy as np
from sklearn.linear_model import RidgeClassifier
from sklearn.metrics import accuracy_score

# Suppose 'xs, ys, xt, yt' were produced in Step 1
# We'll specify a chosen alpha value
alpha_value = 1.0

# Initialize and train the Ridge classifier on the source data only
clf = RidgeClassifier(alpha=alpha_value)
clf.fit(xs, ys)


# Predict on the target data
yt_pred = clf.predict(xt)

    
# Evaluate accuracy on the target domain
ridge_acc = accuracy_score(yt, yt_pred)

    
# We can also view the decision scores for further analysis
ys_score = clf.decision_function(xs)
yt_score = clf.decision_function(xt)
