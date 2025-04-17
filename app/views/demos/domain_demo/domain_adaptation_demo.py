"""
Adapted from PyKale's toy domain adaptation demo:
https://github.com/pykale/pykale/tree/main/examples/toy_domain_adaptation

Author: Shuo Zhou
"""

import streamlit as st
from utils.helper_utils import load_file

from utils.constants import (
    PRIMARY_COLOR, 
    SUBHEADING_COLOR, 
    DEFAULT_SEED
)

from views.demos.domain_demo.domain_backend import (
    run_domain_adaptation_pipeline, 
    show_scatter_plots, 
    show_score_histograms
)

from views.components.ui import (
    info_card,
    page_header,
    section_block,
    code_snippet_block,
    button_component
)


def domain_adaptation_page():
    """
    Domain Adaptation tutorial replicating PyKale's toy_domain_adaptation example.
    Users can follow step-by-step instructions, see visualizations, and experiment.
    """
    # Header
    col_left, col_mid, col_right = st.columns([1, 4, 1])

    with col_mid:
        page_header(
            title="🌐 PyKale Toy Domain Adaptation",
            subtitle="""
            This tutorial walks you through how to adapt a model from one 
            domain (<em>source</em>) to another (<em>target</em>) using 
            <strong>Ridge Classifier</strong> and 
            <strong>CoIRLS</strong> (from PyKale).
            """,
        )

        button_component(
            button_text="🔙 Back to Hub",
            slug="hub"
        )
        

    # Step 1 — Generate Data
    with col_mid:
        section_block(
            title="1. Generate Toy Data",
            heading_level=2,
            color=PRIMARY_COLOR,
            body="""
            We generate two datasets using <code>sklearn.datasets.make_blobs</code>: one for the source domain, 
            one for the target. The target is slightly shifted to simulate domain shift.
            """
        )

        code_snippet_block(
            label="Show the data-generation code",
            code=load_file("code_snippets/domain_adaptation/step1_generate_data.py")
        )

        st.markdown("---")

    # Step 2 — Ridge Classifier
    with col_mid:
        section_block(
            title="2. Train a Ridge Classifier (Baseline)",
            heading_level=2,
            color=PRIMARY_COLOR,
            body="""
            This classifier is trained only on the source data. It doesn’t understand 
            the domain shift, so accuracy on the target may be lower.
            """
        )

        code_snippet_block(
            label="Show the Ridge training code",
            code=load_file("code_snippets/domain_adaptation/step2_ridge_classifier.py")
        )

        st.markdown("---")

    # Step 3 — CoIRLS Adaptation
    with col_mid:
        section_block(
            title="3. Apply Domain Adaptation (CoIRLS)",
            heading_level=2,
            color=PRIMARY_COLOR,
            body="""
            CoIRLS leverages domain covariates to shift the decision boundary. 
            This often improves generalization on the target domain.
            """
        )

        code_snippet_block(
            label="Show the adaptation code",
            code=load_file("code_snippets/domain_adaptation/step3_CoIRLS.py")
        )

        st.markdown("---")

    # Interactive Sliders
    with col_mid:
        section_block("4. Experiment with Hyperparameters")
        alpha_value = st.slider("Ridge alpha (regularization)", 0.1, 3.0, 1.0, 0.1)
        lambda_value = st.slider("CoIRLS lambda (adaptation strength)", 0.1, 3.0, 1.0, 0.1)
        seed_value = st.number_input("Random Seed", min_value=0, value=DEFAULT_SEED, step=1)
        results = run_domain_adaptation_pipeline(alpha_value, lambda_value, seed_value)
        ridge_acc, adapt_acc, ys_score, yt_score, ys_score_adapt, yt_score_adapt, xs, ys, xt, yt = results
        st.markdown("---")

    # Visuals
    with col_mid:
        section_block("5A. Visualize Source & Target Data")
        show_scatter_plots(xs, ys, xt, yt)
        st.markdown("---")

        # Comparison Section
        section_block(
            title="5B. Compare Accuracies",
            body="Let's see how the two classifiers perform on the <strong>target</strong> domain:"
        )

        st.markdown(f"""
        <div style="display:flex; justify-content:center; gap:50px; margin:20px 0;">
            <div style="border:2px solid {PRIMARY_COLOR}; border-radius:5px; padding:10px; text-align:center; width:150px;">
                <p style="color:{SUBHEADING_COLOR}; margin:5px 0; font-size:18px;">Ridge</p>
                <p style="font-size:24px; margin:5px 0;">{ridge_acc:.2f}</p>
                <p style="color:gray; margin:0;">alpha = {alpha_value:.1f}</p>
            </div>
            <div style="border:2px solid {PRIMARY_COLOR}; border-radius:5px; padding:10px; text-align:center; width:150px;">
                <p style="color:{SUBHEADING_COLOR}; margin:5px 0; font-size:18px;">CoIRLS</p>
                <p style="font-size:24px; margin:5px 0;">{adapt_acc:.2f}</p>
                <p style="color:gray; margin:0;">lambda = {lambda_value:.1f}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)


        # Distributions
        section_block("5C. Decision Score Distributions")
        show_score_histograms(ys_score, yt_score, ys_score_adapt, yt_score_adapt)
        st.markdown("---")


    # Summary
    with col_mid:
        info_card(
            title="🧠 Key Takeaways",
            bullets=[
                "<strong>Domain Shift</strong> happens when training and test data distributions differ.",
                "<strong>Ridge vs. CoIRLS:</strong> Ridge ignores domain; CoIRLS accounts for it using covariates.",
                "<strong>Visual Tools</strong> help us understand decision boundaries and scores.",
                "<strong>Hyperparameters Matter:</strong> Tune <code>alpha</code> and <code>lambda</code> for best performance."
            ],
            footer_note="""
            This tutorial demonstrated how domain adaptation improves robustness. 
            Try modifying the data or classifier settings to explore deeper!
            """
        )

