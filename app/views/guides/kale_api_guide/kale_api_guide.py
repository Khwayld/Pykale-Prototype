import streamlit as st
from streamlit_card import card
from utils.constants import MODULES
from navigation.navigation import go_to

from views.components.ui import (
    info_card,
    page_header, 
    section_block,
    button_component
)

def kale_api_page():
    """KALE API home page"""

    # Header
    page_header(
        title="📌 The KALE API Guide",
        subtitle="""
        PyKale follows a modular, pipeline-based approach to machine learning.
        Each module below represents a specific step in the workflow.
        Click on a module to learn more.
        """
    )

    button_component(
        button_text="🔙 Back to Hub",
        slug="hub",
        centering=[3.4, 1, 3]
    )


    # Section header
    section_block(
        title="Select a Module to Explore",
        heading_level=3
    )

    # Display modules
    num_cols = 2
    cols = st.columns(num_cols)
    for i, module in enumerate(MODULES):
        with cols[i % num_cols]:
            card(
                title=module["name"],
                text=module["desc"],
                image="https://avatars.githubusercontent.com/u/63680111?s=200&v=4",
                styles={
                    "card": {
                        "width": "100%",
                        "padding": "15px",
                        "border-radius": "10px",
                        "box-shadow": "0px 4px 8px rgba(0,0,0,0.2)",
                        "cursor": "pointer" 
                    }
                },
                on_click=lambda nav=module["nav"]: go_to(nav),
                key=module["nav"]
            )

    st.write("---")

    # Next steps section
    info_card(
        title="🚀 Next Steps",
        bullets=[
            '📖 <a href="https://pykale.readthedocs.io/" target="_blank">PyKale Documentation</a>',
            '🔬 <a href="https://github.com/pykale/pykale" target="_blank">GitHub Repository</a>'
        ]
    )
