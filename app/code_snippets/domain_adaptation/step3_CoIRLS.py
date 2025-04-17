"""
Adapted from PyKale's toy domain adaptation demo:
https://github.com/pykale/pykale/tree/main/examples/toy_domain_adaptation

Author: Shuo Zhou
"""

import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import accuracy_score
from kale.pipeline.multi_domain_adapter import CoIRLS

    
# Suppose 'xs, ys, xt, yt' and 'N_SAMPLES' were from Steps 1 & 2
# We'll specify a chosen lambda value
lambda_value = 1.0

    
# Build a domain covariate indicating which samples come from source vs. target
covariates = np.zeros(N_SAMPLES * 2)  # total = source samples + target samples
covariates[:N_SAMPLES] = 1            # let's say 1 for source, 0 for target

    
# Encode covariates as one-hot
enc = OneHotEncoder(handle_unknown="ignore")
covariates_mat = enc.fit_transform(covariates.reshape(-1, 1)).toarray()

    
# Concatenate source + target features
x_all = np.concatenate((xs, xt))

    
# We typically train CoIRLS on the combined data (and domain covariates),
# though in many examples we only have labels for the source portion (ys).
# The original PyKale example uses ys for the labeling part.
clf_adapt = CoIRLS(lambda_=lambda_value)
clf_adapt.fit(x_all, ys, covariates_mat)  # passing source labels + domain matrix

    
# Evaluate on the target domain
yt_pred_adapt = clf_adapt.predict(xt)
adapt_acc = accuracy_score(yt, yt_pred_adapt)

    
# Optionally, get decision scores for source/target
ys_score_adapt = clf_adapt.decision_function(xs).detach().numpy().ravel()
yt_score_adapt = clf_adapt.decision_function(xt).detach().numpy().ravel()
