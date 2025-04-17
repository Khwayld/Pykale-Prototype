"""
Adapted from PyKale's toy domain adaptation demo:
https://github.com/pykale/pykale/tree/main/examples/toy_domain_adaptation

Author: Shuo Zhou
"""


import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
from sklearn.datasets import make_blobs
from sklearn.linear_model import RidgeClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import OneHotEncoder
from kale.pipeline.multi_domain_adapter import CoIRLS

from utils.constants import N_SAMPLES, SUBHEADING_COLOR



def run_domain_adaptation_pipeline(alpha_value, lambda_value, seed):
    """
    Runs a toy domain adaptation pipeline using RidgeClassifier and CoIRLS.

    Args:
        alpha_value: Regularization strength for RidgeClassifier.
        lambda_value: Regularization parameter for CoIRLS.
        seed: Random seed for reproducibility.

    Returns:
        Tuple of metrics and intermediate data:
        (ridge_acc, adapt_acc, ys_score, yt_score, ys_score_adapt, yt_score_adapt, xs, ys, xt, yt)
    """
    # Generate toy data with user-defined seed
    np.random.seed(seed)
    xs, ys = make_blobs(N_SAMPLES, centers=[[0, 0], [0, 2]], cluster_std=[0.3, 0.35])
    xt, yt = make_blobs(N_SAMPLES, centers=[[2, -2], [2, 0.2]], cluster_std=[0.35, 0.4])

    # Train base classifier (Ridge)
    clf = RidgeClassifier(alpha=alpha_value)
    clf.fit(xs, ys)
    yt_pred = clf.predict(xt)
    ridge_acc = accuracy_score(yt, yt_pred)
    
    # Decision scores (for visualization)
    ys_score = clf.decision_function(xs)
    yt_score = clf.decision_function(xt)

    # Prepare covariate matrix for CoIRLS
    covariates = np.zeros(N_SAMPLES * 2)
    covariates[:N_SAMPLES] = 1
    covariates_mat = OneHotEncoder(handle_unknown="ignore").fit_transform(
        covariates.reshape(-1, 1)
    ).toarray()

    # Domain adaptation using CoIRLS
    x_all = np.concatenate((xs, xt))
    clf_adapt = CoIRLS(lambda_=lambda_value)
    clf_adapt.fit(x_all, ys, covariates_mat)
    yt_pred_adapt = clf_adapt.predict(xt)
    adapt_acc = accuracy_score(yt, yt_pred_adapt)

    # Decision scores after adaptation
    ys_score_adapt = clf_adapt.decision_function(xs).detach().numpy().ravel()
    yt_score_adapt = clf_adapt.decision_function(xt).detach().numpy().ravel()

    return (
        ridge_acc, adapt_acc,
        ys_score, yt_score,
        ys_score_adapt, yt_score_adapt,
        xs, ys, xt, yt
    )



def show_scatter_plots(xs, ys, xt, yt):
    """
    Visualizes 2D scatter plots for both source and target datasets.

    Args:
        xs: Source input features.
        ys: Source labels.
        xt: Target input features.
        yt: Target labels.
    """
    # Source plot
    st.markdown(f"<h4 style='text-align:center;color:{SUBHEADING_COLOR};'>Source Scatter Plot</h4>", unsafe_allow_html=True)
    
    source_df = pd.DataFrame({
        "x": xs[:, 0],
        "y": xs[:, 1],
        "label": np.where(ys == 1, "Positive", "Negative")
    })

    scatter_src = alt.Chart(source_df).mark_circle(size=60).encode(
        x="x",
        y="y",
        color="label",
        tooltip=["x", "y", "label"]
    ).properties(width=500, height=350)

    col_left, col_mid, col_right = st.columns([2,4,2])
    with col_mid:
        st.altair_chart(scatter_src, use_container_width=False)

    # Target plot
    st.markdown(f"<h4 style='text-align:center;color:{SUBHEADING_COLOR};'>Target Scatter Plot</h4>", unsafe_allow_html=True)
    
    target_df = pd.DataFrame({
        "x": xt[:, 0],
        "y": xt[:, 1],
        "label": np.where(yt == 1, "Positive", "Negative")
    })

    scatter_tgt = alt.Chart(target_df).mark_circle(size=60).encode(
        x="x",
        y="y",
        color="label",
        tooltip=["x", "y", "label"]
    ).properties(width=500, height=350)


    col_left, col_mid, col_right = st.columns([2,4,2])
    with col_mid:
        st.altair_chart(scatter_tgt, use_container_width=False)


def show_score_histograms(ys_score, yt_score, ys_score_adapt, yt_score_adapt):
    """
    Plots histograms of decision scores from both the Ridge and CoIRLS classifiers.

    Args:
        ys_score: Source scores from Ridge.
        yt_score: Target scores from Ridge.
        ys_score_adapt: Source scores from CoIRLS.
        yt_score_adapt: Target scores from CoIRLS.
    """
    # Ridge histogram
    st.markdown(f"<h4 style='text-align:center;color:{SUBHEADING_COLOR};'>Ridge Classifier Score Distribution</h4>", unsafe_allow_html=True)
    
    ridge_data = pd.DataFrame({
        'Score': np.concatenate([ys_score, yt_score]),
        'Type': (['Source'] * len(ys_score)) + (['Target'] * len(yt_score))
    })
    
    ridge_hist = alt.Chart(ridge_data).mark_bar(opacity=0.6).encode(
        x=alt.X('Score:Q', bin=alt.Bin(maxbins=30), title='Decision Scores'),
        y=alt.Y('count()', title='Count'),
        color=alt.Color(
            'Type:N',
            scale=alt.Scale(domain=['Source','Target'], range=['#FF0000','#0000FF'])
        )
    ).properties(width=500, height=350)

    col_left, col_mid, col_right = st.columns([2,4,2])
    with col_mid:
        st.altair_chart(ridge_hist, use_container_width=False)

    # CoIRLS histogram
    st.markdown(f"<h4 style='text-align:center;color:{SUBHEADING_COLOR};'>CoIRLS Adaptation Score Distribution</h4>", unsafe_allow_html=True)
    
    adapt_data = pd.DataFrame({
        'Score': np.concatenate([ys_score_adapt, yt_score_adapt]),
        'Type': (['Source'] * len(ys_score_adapt)) + (['Target'] * len(yt_score_adapt))
    })

    adapt_hist = alt.Chart(adapt_data).mark_bar(opacity=0.6).encode(
        x=alt.X('Score:Q', bin=alt.Bin(maxbins=30), title='Decision Scores'),
        y=alt.Y('count()', title='Count'),
        color=alt.Color(
            'Type:N',
            scale=alt.Scale(domain=['Source','Target'], range=['#FF0000','#0000FF'])
        )
    ).properties(width=500, height=350)

    col_left, col_mid, col_right = st.columns([2,4,2])
    with col_mid:
        st.altair_chart(adapt_hist, use_container_width=False)


