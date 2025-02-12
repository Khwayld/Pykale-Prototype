import streamlit as st
from chatbot.chatbot import display_chatbot


def home_page():
    st.markdown("<h1 style='text-align: center;'>Welcome To PyKale 👋</h1>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center;'>A library built upon PyTorch for multimodal learning and transfer learning from multiple data sources</h5>", unsafe_allow_html=True)
    st.write("---")
    st.subheader("Chat with Our PyKale Bot")
    display_chatbot()
