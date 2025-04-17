import streamlit as st
from utils.constants import SUBHEADING_COLOR

from views.components.ui import (
    info_card,
    page_header, 
    section_block,
    button_component
)

def home_page():
    """
    Home Page 
    """
    # Header
    page_header(
        title="👋 Welcome to The PyKale Hub",
        subtitle="""
        Our mission is to make <strong>PyKale</strong> more accessible by providing 
        interactive guides, tutorials, and demos for machine learning and multimodal learning.
        """
    )

    st.write("---")

    # Info section
    info_card(
        title="🌟 What This Website Offers",
        bullets=[
            "🛠️ <strong>Interactive Examples</strong> - Run PyKale code live in your browser.",
            "📖 <strong>Guided Tutorials</strong> - Learn key concepts step by step.",
            "🚀 <strong>Practical Use Cases</strong> - See PyKale applied to real-world problems.",
            "🔗 <strong>Community & Resources</strong> - Get support and contribute to PyKale."
        ],
        color=SUBHEADING_COLOR
    )


    # Chatbot section
    section_block(
        title="💬 Need Help? Try the PyKale Assistant",
        body="Ask questions, get guidance, and explore PyKale interactively.",
        heading_level=3,
        color=SUBHEADING_COLOR
    )
    
    button_component(
        button_text="💬 Chat with Assistant",
        slug="chatbot_page",
        centering=[3.1, 1, 3]
    )
