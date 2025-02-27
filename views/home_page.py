import streamlit as st
from views.chatbot import display_chatbot

def home_page():
    """Streamlit Home Page for PyKale Hub with Centered Content & Chatbot."""
    
    # Title
    st.markdown(
        """
        <div style="text-align:center;">
            <h1>👋 Welcome To The PyKale Hub</h1>
            <p style="font-size:18px;">
                Our mission is to make <strong>PyKale</strong> more accessible by providing 
                interactive guides, tutorials, and demos for machine learning and multimodal learning.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("---")

    # Section
    st.markdown(
        """
        <div style="text-align:center;">
            <h3>🌟 What This Website Offers</h3>
            <ul style="display: inline-block; text-align: left;">
                <li>🛠️ <strong>Interactive Examples</strong> - Run PyKale code live in your browser.</li>
                <li>📖 <strong>Guided Tutorials</strong> - Learn key concepts step by step.</li>
                <li>🚀 <strong>Practical Use Cases</strong> - See PyKale applied to real-world problems.</li>
                <li>🔗 <strong>Community & Resources</strong> - Get support and contribute to PyKale.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("---")

    # Chatbot Section
    st.markdown(
        """
        <div style="text-align:center;">
            <h3>💬 Need Help? Try the PyKale Assistant</h3>
            <p>Ask questions, get guidance, and explore PyKale interactively.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
