import streamlit as st
from helpers.constants import (
    PRIMARY_COLOR, 
    SUBHEADING_COLOR, 
    DEFAULT_SEED
)

from helpers.domain_utils import (
    run_domain_adaptation_pipeline, 
    show_scatter_plots, 
    show_score_histograms
)

from navigation import go_to



def domain_adaptation_page():
    """
    A step-by-step Streamlit tutorial replicating PyKale's toy_domain_adaptation
    example (https://github.com/pykale/pykale/blob/main/examples/toy_domain_adaptation/tutorial.ipynb). 
    Each step shows the relevant code and a brief explanation.
    """

    col_left, col_mid, col_right = st.columns([1, 4, 1])

    # ----------------------------------------------------------------------------
    # 1. INTRO & PAGE HEADER
    # ----------------------------------------------------------------------------
    with col_mid:
        st.markdown(
            f"""
            <div style="text-align: center;">
                <h1>🌐 PyKale Toy Domain Adaptation (Step by Step)</h1>
                <p style="font-size:16px; max-width:700px; margin:auto;">
                This tutorial walks you through how to adapt a model from one 
                domain (<em>source</em>) to another (<em>target</em>) using 
                <strong>Ridge Classifier</strong> and 
                <strong>CoIRLS</strong> (from PyKale).
                </p>
            </div>
            """, 
            unsafe_allow_html=True
        )


        col_left, col_center, col_right = st.columns([3, 1.5, 3])
        with col_center:
            if st.button("🔙 Back to Hub"):
                go_to("hub")

        st.markdown("---")

    # ----------------------------------------------------------------------------
    # 2. CODE SECTIONS & EXPLANATIONS
    # ----------------------------------------------------------------------------

    # --- Step 1: Generate Toy Data ---
    with col_mid:
        st.markdown(
            f"<h2 style='text-align:center; color:{SUBHEADING_COLOR};'>1. Generate Toy Data</h2>",
            unsafe_allow_html=True
        )

        st.write("""
        We create two sets of blob data (source & target) using 
        **`sklearn.datasets.make_blobs`**. The target set is slightly shifted to mimic
        a real-world scenario where the domain we want to predict on differs from our
        training domain.
        """)

        with st.expander("Show the data-generation code"):
            st.code("""
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
            """)

        st.markdown("---")

    # --- Step 2: BASELINE CLASSIFIER (RIDGE) ---
    with col_mid:
        st.markdown(
            f"<h2 style='text-align:center; color:{SUBHEADING_COLOR};'>2. Train a Ridge Classifier (Baseline)</h2>",
            unsafe_allow_html=True
        )
        st.write("""
            We first train a simple **RidgeClassifier** 
            on the source data **only**. It doesn't know that there's 
            a distinct target domain, so performance on the target might be suboptimal.
        """)

        with st.expander("Show the Ridge training code from domain_utils.py"):
            st.code("""
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
            """)

        st.markdown("---")

    # --- Step 3: DOMAIN ADAPTATION WITH CoIRLS ---
    with col_mid:
        st.markdown(
            f"<h2 style='text-align:center; color:{SUBHEADING_COLOR};'>3. Apply Domain Adaptation (CoIRLS)</h2>",
            unsafe_allow_html=True
        )
        st.write("""
            **CoIRLS** explicitly leverages domain covariates (i.e., 
            whether a sample is from the source or target) to adjust its decision boundary. 
            This can often yield better performance on the target domain.
        """, unsafe_allow_html=True)


        with st.expander("Show the adaptation code from domain_utils.py"):
            st.code("""
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
            """)

        st.markdown("---")

    # --------------------------------------------------------------------
    # 3) INTERACTIVE DEMO
    # --------------------------------------------------------------------
    with col_mid:
        st.markdown(
            f"<h2 style='text-align:center; color:{SUBHEADING_COLOR};'>4. Experiment with Hyperparameters</h2>",
            unsafe_allow_html=True
        )

        st.write("""
            Use the sliders below to set the regularization strength for Ridge 
            (`alpha`) and the adaptation strength for CoIRLS 
            (`lambda`), then see how accuracies change!
        """)

        # Sliders
        alpha_value = st.slider("Ridge alpha (regularization)", 0.1, 3.0, 1.0, 0.1)
        lambda_value = st.slider("CoIRLS lambda (adaptation strength)", 0.1, 3.0, 1.0, 0.1)
        seed_value = st.number_input("Random Seed", min_value=0, value=DEFAULT_SEED, step=1)

        # Run pipeline
        ridge_acc, adapt_acc, ys_score, yt_score, ys_score_adapt, yt_score_adapt, xs, ys, xt, yt = (
            run_domain_adaptation_pipeline(
                alpha_value=alpha_value,
                lambda_value=lambda_value,
                seed=seed_value
            )
        )

        st.markdown("---")

    # --- Scatter Plots ---
    with col_mid:
        st.markdown(
            f"<h2 style='text-align:center; color:{SUBHEADING_COLOR};'>5A. Visualize Source & Target Data</h2>",
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <p style="text-align:center;">
            Here's how our source and target data look. 
            Notice the shift in the cluster centers (the 'domain shift').
            </p>
            """,
            unsafe_allow_html=True
        )

        show_scatter_plots(xs, ys, xt, yt)

        st.markdown("---")

    # --- Compare Classifier Accuracies ---
    with col_mid:
        st.markdown(
            f"<h2 style='text-align:center; color:{SUBHEADING_COLOR};'>5B. Compare Accuracies</h2>",
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <p style="text-align:center;">
            Let's see how the two classifiers perform on the 
            <strong>target</strong> domain:
            </p>
            """,
            unsafe_allow_html=True
        )

        st.markdown(f"""
        <div style="display:flex; justify-content:center; gap:50px; margin:20px 0;">
            <div style="border:2px solid {SUBHEADING_COLOR}; border-radius:5px; padding:10px; text-align:center; width:150px;">
                <p style="color:{SUBHEADING_COLOR}; margin:5px 0; font-size:18px;">Ridge</p>
                <p style="font-size:24px; margin:5px 0;">{ridge_acc:.2f}</p>
                <p style="color:gray; margin:0;">alpha = {alpha_value:.1f}</p>
            </div>
            <div style="border:2px solid {SUBHEADING_COLOR}; border-radius:5px; padding:10px; text-align:center; width:150px;">
                <p style="color:{SUBHEADING_COLOR}; margin:5px 0; font-size:18px;">CoIRLS</p>
                <p style="font-size:24px; margin:5px 0;">{adapt_acc:.2f}</p>
                <p style="color:gray; margin:0;">lambda = {lambda_value:.1f}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(
            """
            <p style="text-align:center;">
            Generally, <strong>CoIRLS</strong> achieves better performance on the 
            target domain by leveraging domain covariates.
            </p>
            """,
            unsafe_allow_html=True
        )

        st.markdown("---")

    # --- Score Distributions ---
    with col_mid:
        st.markdown(
            f"<h2 style='text-align:center; color:{SUBHEADING_COLOR};'>5C. Decision Score Distributions</h2>",
            unsafe_allow_html=True
        )
        st.write("""
            Finally, let's look at the decision score histograms for each classifier, 
            showing how the <em>source</em> vs. <em>target</em> score distributions compare.
        """, unsafe_allow_html=True)

        show_score_histograms(ys_score, yt_score, ys_score_adapt, yt_score_adapt)

        st.markdown("---")

    # --------------------------------------------------------------------
    # 4) Summary
    # --------------------------------------------------------------------
    with col_mid:
        st.markdown(
            f"<h2 style='text-align:center; color:{SUBHEADING_COLOR};'>6. Key Takeaways</h2>",
            unsafe_allow_html=True
        )

        st.write("""
        - **Domain Shifts** happen when training data and real-world data differ.
        - **Ridge vs. CoIRLS**: A simple classifier ignores domain differences; 
          an adaptation method accounts for them.
        - **Scores & Visuals**: Plots help us see how well each classifier separates classes.
        - **Hyperparameters**: Both `alpha` and `lambda` matter—experiment to find optimal values.
        """)

        st.write("""
            **That’s the end of our step-by-step Domain Adaptation tutorial!** 
            Use the sliders above to experiment. 
            We hope this clarifies how domain adaptation techniques can help 
            models perform better when data distributions shift in practice.
        """)

        st.markdown("---")

