import streamlit as st

from views.components.ui import (
    info_card,
    page_header,
    section_block,
    button_component
)

def introduction_page():
    """Getting Started With PyKale"""

    # Header
    page_header(
        title="📖 Getting Started with PyKale",
        subtitle="An introduction to PyKale, its purpose, and how to use it."
    )

    button_component(
        button_text="🔙 Back to Hub",
        slug="hub",
        centering=[3.4, 1, 3]
    )

    # Overview
    section_block(
        title="🧠 What is PyKale?",
        body="""
        PyKale is an open-source Python library for <strong>knowledge-aware machine learning</strong>, 
        enabling learning from multiple data sources, including <strong>multimodal learning</strong> 
        and <strong>transfer learning</strong>. 
        """,
        heading_level=3
    )

    section_block(
        title="",
        body="""
        The library was originally designed to support <strong>healthcare applications</strong> 
        and interdisciplinary research. The name <em>Kale</em> was chosen after the healthy vegetable 
        to reflect its goal of supporting sustainable machine learning research.
        """
    )

    st.write("---")

    # Objectives
    info_card(
        title="🎯 Objectives",
        bullets=[
            "♻️ <strong>Reducing redundancy</strong> – Standardizing workflows and refactoring code.",
            "🛠️ <strong>Reusing existing resources</strong> – Leveraging existing models and libraries.",
            "🔗 <strong>Recycling learning models</strong> – Applying models across different applications."
        ]
    )


    # Installation
    info_card(
        title="⚙️ Requirements",
        bullets=[
            "🐍 Python <strong>3.9, 3.10,</strong> or <strong>3.11</strong>",
            "⚡ PyTorch (Ensure it matches your hardware: CPU or GPU)",
            "📊 (Optional) PyTorch Geometric (for graph-based tasks)"
        ]
    )

    # PyKale Workflow
    info_card(
        title="🛠️ <strong>PyKale Workflow Example</strong>",
        subtitle="PyKale follows a <strong>standardized machine learning workflow</strong>, where each module serves a specific function:",
        bullets=[
            "📂 <strong>Load Data</strong> (<code>loaddata</code>) – Loads data from disk or online resources.",
            "⚙️ <strong>Preprocess Data</strong> (<code>prepdata</code>) – Transforms and prepares data for machine learning models.",
            "📑 <strong>Embed</strong> (<code>embed</code>) – Maps data into a new space to extract or select features.",
            "🔍 <strong>Predict</strong> (<code>predict</code>) – Generates predictions based on trained models.",
            "📊 <strong>Evaluate</strong> (<code>evaluate</code>) – Assesses model performance using defined metrics.",
            "🔎 <strong>Interpret</strong> (<code>interpret</code>) – Analyzes features and predictions, mainly via visualization.",
            "🔗 <strong>Pipeline</strong> (<code>pipeline</code>) – Specifies a full machine learning workflow by combining multiple modules."
        ]
    )