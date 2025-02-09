import numpy as np
from sklearn.datasets import make_blobs
from sklearn.linear_model import RidgeClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import OneHotEncoder
from kale.pipeline.multi_domain_adapter import CoIRLS
import streamlit as st
import pandas as pd
import altair as alt


# CONSTANTS
N_SAMPLES = 200


def generate_toy_data():
    np.random.seed(29118)
    # Generate toy data
    xs, ys = make_blobs(N_SAMPLES, centers=[[0, 0], [0, 2]], cluster_std=[0.3, 0.35])
    xt, yt = make_blobs(N_SAMPLES, centers=[[2, -2], [2, 0.2]], cluster_std=[0.35, 0.4])

    return xs, ys, xt, yt

def generate_ridge_data(xs, ys, xt, yt):
    clf = RidgeClassifier(alpha=1.0)
    clf.fit(xs, ys)

    yt_pred = clf.predict(xt)
    accuracy = accuracy_score(yt, yt_pred)

    ys_score = clf.decision_function(xs)
    yt_score = clf.decision_function(xt)

    return accuracy, ys_score, yt_score


def generate_domain_data(xs, ys, xt, yt):
    clf_ = CoIRLS(lambda_=1)
    
    covariates = np.zeros(N_SAMPLES * 2)
    covariates[:N_SAMPLES] = 1
    enc = OneHotEncoder(handle_unknown="ignore")
    covariates_mat = enc.fit_transform(covariates.reshape(-1, 1)).toarray()

    x = np.concatenate((xs, xt))
    clf_.fit(x, ys, covariates_mat)
    yt_pred_ = clf_.predict(xt)
    accuracy = accuracy_score(yt, yt_pred_)

    ys_score = clf_.decision_function(xs).detach().numpy().reshape(-1)
    yt_score = clf_.decision_function(xt).detach().numpy().reshape(-1)

    return accuracy, ys_score, yt_score



def domain_adaptation_example():    
    # generate data for app to use
    xs, ys, xt, yt = generate_toy_data() 
    acc, ys_score, yt_score = generate_ridge_data(xs, ys, xt, yt)
    acc_, ys_score_, yt_score_ = generate_domain_data(xs, ys, xt, yt)    

    # create scatter plot for source
    st.title("Scatter Plot For Source")
    chart_data = pd.DataFrame({
        "x": xs[:, 0],
        "y": xs[:, 1],
        "label": np.where(ys == 1, "Positive", "Negative")
    })

    scatter_data = alt.Chart(chart_data).mark_circle().encode(
        x="x", 
        y="y", 
        color="label",
        tooltip=["x", "y", "label"]
    )
    
    st.altair_chart(
        scatter_data, 
        use_container_width=True
    )


    # create scatter plot for target
    st.title("Scatter Plot For Target")
    chart_data = pd.DataFrame({
        "x": xt[:, 0],
        "y": xt[:, 1],
        "label": np.where(yt == 1, "Positive", "Negative")
    })

    scatter_data = alt.Chart(chart_data).mark_circle().encode(
        x="x", 
        y="y", 
        color="label",
        tooltip=["x", "y", "label"]
    )
    
    st.altair_chart(
        scatter_data, 
        use_container_width=True
    )


    # create text elements
    st.write("Accuracy on target domain: {:.2f}".format(acc))
    st.write("Accuracy on target domain: {:.2f}".format(acc_))


    # Create histogram for ridge classifier    
    data = pd.DataFrame({
        'Score': np.concatenate([ys_score, yt_score]),
        'Type': ['Source'] * len(ys_score) + ['Target'] * len(yt_score)
    })

    chart = alt.Chart(data).mark_bar(opacity=0.6).encode(
        x=alt.X('Score:Q', bin=alt.Bin(maxbins=30), title='Decision Scores'),
        y=alt.Y('count()', title='Count'),
        color=alt.Color('Type:N', scale=alt.Scale(domain=['Source', 'Target'], range=['#FF0000', '#0000FF']))
    )

    st.title("Ridge classifier decision score distribution")
    st.altair_chart(chart, use_container_width=True)




    # Create histogram for Domain Adaptation Classifier    
    data = pd.DataFrame({
        'Score': np.concatenate([ys_score_, yt_score_]),
        'Type': ['Source'] * len(ys_score_) + ['Target'] * len(yt_score_)
    })

    chart = alt.Chart(data).mark_bar(opacity=0.6).encode(
        x=alt.X('Score:Q', bin=alt.Bin(maxbins=30), title='Decision Scores'),
        y=alt.Y('count()', title='Count'),
        color=alt.Color('Type:N', scale=alt.Scale(domain=['Source', 'Target'], range=['#FF0000', '#0000FF']))
    )

    st.title("Domain adaptation classifier decision score distribution")
    st.altair_chart(chart, use_container_width=True)




