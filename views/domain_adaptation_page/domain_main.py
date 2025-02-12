import streamlit as st
from helpers.constants import PRIMARY_COLOR, SUBHEADING_COLOR, DEFAULT_SEED
from .domain_utils import run_domain_adaptation_pipeline, show_scatter_plots, show_score_histograms




def domain_adaptation_page():
    st.markdown(f"""
    <div style="background-color:{PRIMARY_COLOR};padding:20px;border-radius:10px;margin-bottom:20px;text-align:center;">
        <h1 style="color:white;margin:0;">🌐 Domain Adaptation Example</h1>
        <p style="color:#ecf0f1;font-size:18px;margin:5px 0 0;">
            Adapt a model from one domain (source) to another (target) using PyKale.
        </p>
    </div>
    """, unsafe_allow_html=True)


    # 1. Overview
    st.markdown("<hr style='border:1px solid #bdc3c7;'>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align:center;color:{PRIMARY_COLOR};'>1. Overview & Why It Matters</h2>", unsafe_allow_html=True)
    st.markdown("""
    <p style="text-align:center;font-size:16px;">
      In many cases, data from one domain (source) does not perfectly match 
      data from another domain (target). Domain adaptation helps your model
      perform better on the target by leveraging source data in a smarter way.
    </p>
    """, unsafe_allow_html=True)

    st.markdown("<hr style='border:1px solid #bdc3c7;'>", unsafe_allow_html=True)

    # 2. How it works
    st.markdown(f"<h2 style='text-align:center;color:{PRIMARY_COLOR};'>2. How It Works</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div style="display:flex; justify-content:center;">
        <ol style="list-style:none; padding-left:0;">
          <li style="margin-bottom:10px;">
            <span style="font-size:24px;">✨</span>
            <strong style="font-size:16px;">Generate Two Blobs</strong><br/>
            <span style="color:#7f8c8d;">We create synthetic source and target blobs with slight differences.</span>
          </li>
          <li style="margin-bottom:10px;">
            <span style="font-size:24px;">🔧</span>
            <strong style="font-size:16px;">Train Two Classifiers</strong><br/>
            <span style="color:#7f8c8d;">A simple Ridge Classifier vs. <em>CoIRLS</em> from PyKale for adaptation.</span>
          </li>
          <li style="margin-bottom:10px;">
            <span style="font-size:24px;">📊</span>
            <strong style="font-size:16px;">Compare Results</strong><br/>
            <span style="color:#7f8c8d;">View accuracy on the target domain and distribution of decision scores.</span>
          </li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr style='border:1px solid #bdc3c7;'>", unsafe_allow_html=True)

    # 3. Interactive Demo
    st.markdown(f"<h2 style='text-align:center;color:{PRIMARY_COLOR};'>3. Interactive Demo</h2>", unsafe_allow_html=True)

    # User controls
    st.markdown("**Model Parameters**")

    col1, col2 = st.columns(2)

    with col1:
        alpha_value = st.slider("Ridge alpha", min_value=0.1, max_value=3.0, value=1.0, step=0.1)
    with col2:
        lambda_value = st.slider("CoIRLS lambda", min_value=0.1, max_value=3.0, value=1.0, step=0.1)

    st.markdown("**Random Seed**")
    seed_value = st.number_input("Seed for Data Generation", min_value=0, value=DEFAULT_SEED, step=1)

    # Run the example from the functions
    ridge_acc, adapt_acc, ys_score, yt_score, ys_score_adapt, yt_score_adapt, xs, ys, xt, yt = run_domain_adaptation_pipeline(
        alpha_value, lambda_value, seed_value
    )

    
    # Show the final accuracies
    st.markdown(f"<h4 style='text-align:center;color:{PRIMARY_COLOR};margin-top:30px;'>Final Accuracies</h4>", 
                unsafe_allow_html=True)
    
    colR_left, colR_mid, colR_right = st.columns([1,2,1])
    with colR_mid:
        st.markdown(f"""
        <div style="display:flex; justify-content:center; gap:30px; margin-bottom:20px;">
            <div style="border:2px solid {SUBHEADING_COLOR}; border-radius:5px; padding:10px; width:150px; text-align:center;">
                <p style="font-size:26px; margin:5px 0; color:{SUBHEADING_COLOR}; text-align:center;">Ridge</p>
                <p style="font-size:20px; margin:5px 0; text-align:center;"><strong>{ridge_acc:.2f}</strong></p>
                <p style="color:#7f8c8d; margin:0; text-align:center;">(alpha={alpha_value:.1f})</p>
            </div>
            <div style="border:2px solid {SUBHEADING_COLOR}; border-radius:5px; padding:10px; width:150px; text-align:center;">
                <p style="font-size:26px; margin:5px 0; color:{SUBHEADING_COLOR}; text-align:center;">CoIRLS</p>
                <p style="font-size:20px; margin:5px 0; text-align:center;"><strong>{adapt_acc:.2f}</strong></p>
                <p style="color:#7f8c8d; margin:0; text-align:center;">(lambda={lambda_value:.1f})</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <p style="text-align:center; font-size:14px; color:#7f8c8d;">
      Generally, <strong>CoIRLS</strong> can achieve better target accuracy by adapting to domain shifts.
    </p>
    """, unsafe_allow_html=True)


    # Display scatter plots
    st.markdown(f"<h4 style='text-align:center;color:{PRIMARY_COLOR};'>Scatter Plots (Source & Target)</h4>", 
                unsafe_allow_html=True)
    show_scatter_plots(xs, ys, xt, yt)

    # Show histograms
    st.markdown(f"<h4 style='text-align:center;color:{PRIMARY_COLOR};'>Decision Score Distributions</h4>", 
                unsafe_allow_html=True)
    show_score_histograms(ys_score, yt_score, ys_score_adapt, yt_score_adapt)


    # 4. Under the Hood
    st.markdown("<hr style='border:1px solid #bdc3c7;'>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align:center;color:{PRIMARY_COLOR};'>4. Under the Hood</h2>", unsafe_allow_html=True)
    with st.expander("Click to see example code snippet"):
        st.code("""
            # We will fill this out later...
        """)
    st.markdown("<hr style='border:1px solid #bdc3c7;'>", unsafe_allow_html=True)


    # 5. Key Takeaways
    st.markdown(f"<h2 style='text-align:center;color:{PRIMARY_COLOR};'>5. Key Takeaways</h2>", unsafe_allow_html=True)
    st.markdown("""
    <ul style="list-style:none; padding-left:0; text-align:left; max-width:600px; margin:auto;">
      <li style="margin-bottom:8px;">
        <span style="font-size:24px; margin-right:8px;">🚀</span>
        <strong>Ridge Classifier</strong> 
        <br/>A simple baseline that doesn't consider domain differences.
      </li>
      <li style="margin-bottom:8px;">
        <span style="font-size:24px; margin-right:8px;">🔗</span>
        <strong>CoIRLS Adaptation</strong>
        <br/>Leverages domain covariates to adjust decision boundaries for better target accuracy.
      </li>
      <li style="margin-bottom:8px;">
        <span style="font-size:24px; margin-right:8px;">🏆</span>
        <strong>Fine-Tune Parameters</strong>
        <br/>Experiment with alpha & lambda to see how they affect performance.
      </li>
    </ul>
    """, unsafe_allow_html=True)
