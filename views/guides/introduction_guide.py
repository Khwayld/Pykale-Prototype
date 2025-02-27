import streamlit as st


def introduction_page():
    """Getting Started With PyKale"""

    # Title
    st.markdown(
        """
        <div style="text-align:center;">
            <h1>📖 Getting Started with PyKale</h1>
            <p style="font-size:18px;">
                An introduction to PyKale, its purpose, and how to use it.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("---")

    # 1. Overview
    st.markdown(
        """
        <div style="text-align:center; max-width:800px; margin:auto;">
            <h3>🧠 What is PyKale?</h3>
            <p>
                PyKale is an open-source Python library for <strong>knowledge-aware machine learning</strong>, 
                enabling learning from multiple data sources, including <strong>multimodal learning</strong> 
                and <strong>transfer learning</strong>. 
            </p>
            <p>
                The library was originally designed to support <strong>healthcare applications</strong> 
                and interdisciplinary research. The name <em>Kale</em> was chosen after the healthy vegetable 
                to reflect its goal of supporting sustainable machine learning research.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.write("---")

    # 2. Objectives
    st.markdown(
        """
        <div style="text-align:center; max-width:800px; margin:auto;">
            <h3>🎯 Objectives</h3>
            <p>PyKale is designed to build <strong>green and efficient machine learning systems</strong> by:</p>
            <ul style="display: inline-block; text-align: left;">
                <li>♻️ <strong>Reducing redundancy</strong> – Standardizing workflows and refactoring code.</li>
                <li>🛠️ <strong>Reusing existing resources</strong> – Leveraging existing models and libraries.</li>
                <li>🔗 <strong>Recycling learning models</strong> – Applying models across different applications.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.write("---")


    # 3. Installation
    st.markdown(
        """
        <div style="text-align:center; max-width:800px; margin:auto;">
            <h3>⚙️ Installation</h3>
            <p><strong>Prerequisites:</strong></p>
            <ul style="display: inline-block; text-align: left;">
                <li>🐍 Python <strong>3.8, 3.9,</strong> or <strong>3.10</strong></li>
                <li>⚡ PyTorch (Ensure it matches your hardware: CPU or GPU)</li>
                <li>📊 (Optional) PyTorch Geometric (for graph-based tasks)</li>
            </ul>
            <p><strong>Install PyKale via pip:</strong></p>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns([1, 2, 1])  
    with col2:
        st.code("pip install pykale", language="bash")

    st.write("---")

    # 4. PyKale Workflow Example
    st.markdown(
        """
        <div style="text-align:center; max-width:800px; margin:auto;">
            <h3>🛠️ <strong>PyKale Workflow Example</strong></h3>
            <p>PyKale follows a <strong>standardized machine learning workflow</strong>, where each module serves a specific function:</p>
            <ul style="display: inline-block; text-align: left;">
                <li>📂 <strong>Load Data</strong> (<code>loaddata</code>) – Loads data from disk or online resources.</li>
                <li>⚙️ <strong>Preprocess Data</strong> (<code>prepdata</code>) – Transforms and prepares data for machine learning models.</li>
                <li>📑 <strong>Embed</strong> (<code>embed</code>) – Maps data into a new space to extract or select features.</li>
                <li>🔍 <strong>Predict</strong> (<code>predict</code>) – Generates predictions based on trained models.</li>
                <li>📊 <strong>Evaluate</strong> (<code>evaluate</code>) – Assesses model performance using defined metrics.</li>
                <li>🔎 <strong>Interpret</strong> (<code>interpret</code>) – Analyzes features and predictions, mainly via visualization.</li>
                <li>🔗 <strong>Pipeline</strong> (<code>pipeline</code>) – Specifies a full machine learning workflow by combining multiple modules.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("---")

    # 5. Next Step
    st.markdown(
        """
        <div style="text-align:center; max-width:800px; margin:auto;">
            <h3>🚀 Next Steps</h3>
            <p>Now that you understand PyKale, check out the following resources:</p>
            <ul style="display: inline-block; text-align: left;">
                <li>📖 <a href="https://pykale.readthedocs.io/" target="_blank">Official PyKale Documentation</a></li>
                <li>🔬 <a href="https://github.com/pykale/pykale" target="_blank">PyKale GitHub Repository</a></li>
                <li>📊 <a href="" target="_self">Guide 1</a></li>
                <li>📑 <a href="" target="_self">Guide 2</a></li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

