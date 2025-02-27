import streamlit as st


def kale_api_page():
    """The KALE API - Detailed Breakdown of how it works"""

    # 📌 Introduction
    st.markdown(
        """
        <div style="text-align:center;">
            <h2>📌 The KALE API</h2>
            <p style="font-size:18px;">
                A detailed breakdown of how the PyKale API works.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.write("---")

    # 1️⃣ Data Handling
    st.markdown(
        """
        <div style="text-align:center;">
            <h3>1️⃣ Data Handling - <code>(kale.loaddata)</code></h3>
            <p>Handles loading datasets such as images, videos, and graphs.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns([1, 2, 1])  
    with col2:
        st.code("""
        from kale.loaddata.image_access import DigitDataset

        # Load the MNIST dataset
        dataset = DigitDataset(dataset_name="MNIST", train=True, download=True)
        """, language="python")

    st.write("---")

    # 2️⃣ Data Preprocessing
    st.markdown("<h4 style='text-align: center;'>2️⃣ Data Preprocessing - <code>(kale.prepdata)</h4>", unsafe_allow_html=True)
    st.write("---")

    # 3️⃣ Feature Extraction & Embedding
    st.markdown("<h4 style='text-align: center;'>3️⃣ Feature Extraction & Embedding - <code>(kale.embed)</h4>", unsafe_allow_html=True)
    st.write("---")

    # 4️⃣ Model Prediction
    st.markdown("<h4 style='text-align: center;'>4️⃣ Model Prediction - <code>(kale.predict)</h4>", unsafe_allow_html=True)
    st.write("---")

    # 5️⃣ Evaluation
    st.markdown("<h4 style='text-align: center;'>5️⃣ Evaluation - <code>(kale.evaluate)</h4>", unsafe_allow_html=True)
    st.write("---")

    # 6️⃣ interpret
    st.markdown("<h4 style='text-align: center;'>6️⃣ Interpretation - <code>(kale.interpret)</h4>", unsafe_allow_html=True)
    st.write("---")

    # 7️⃣ pipeline
    st.markdown("<h4 style='text-align: center;'>7️⃣ Pipeline - <code>(kale.pipeline)</h4>", unsafe_allow_html=True)
    st.write("---")

    # 📌 Full Example: Putting Everything Together
    st.markdown(
        """
        <div style="text-align:center;">
            <h3>📌 Full Example: Putting Everything Together</h3>
            <p>Here's how you can use multiple PyKale modules in one pipeline.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.write("---")

    # 📌 Summary
    st.markdown(
        """
        <div style="text-align:center;">
            <h3>📌 Summary</h3>
            <p>PyKale follows a modular, pipeline-based approach to machine learning:</p>
            <ul style="display: inline-block; text-align: left;">
                <li>📂 <strong>Load Data</strong> - Supports images, videos, and graphs.</li>
                <li>⚙️ <strong>Preprocess</strong> - Transforms data for modeling.</li>
                <li>📑 <strong>Embed</strong> - Extracts useful representations.</li>
                <li>🔍 <strong>Predict</strong> - Builds and applies ML models.</li>
                <li>📊 <strong>Evaluate</strong> - Measures performance.</li>
                <li>🔎 <strong>Interpret</strong> - Visualizes and explains results.</li>
                <li>🔗 <strong>Pipeline</strong> - Combines all steps into a unified workflow.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.write("---")

    # 📌 Next Step
    st.markdown(
        """
        <div style="text-align:center;">
            <h3>🚀 Next Steps</h3>
            <p>Now that you understand the PyKale API, here’s where you can go next:</p>
            <ul style="display: inline-block; text-align: left;">
                <li>📖 <a href="https://pykale.readthedocs.io/" target="_blank">Read the PyKale Documentation</a></li>
                <li>🔬 <a href="https://github.com/pykale/pykale" target="_blank">Explore the PyKale GitHub Repository</a></li>
                <li>📊 <a href="" target="_self">Demo</a></li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
