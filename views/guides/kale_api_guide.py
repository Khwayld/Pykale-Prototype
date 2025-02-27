import streamlit as st


def kale_api_page():
    """The KALE API - Detailed Breakdown of how it works"""

    # 📌 Introduction
    st.markdown("<h4 style='text-align: center;'>📌 Introduction</h4>", unsafe_allow_html=True)
    st.write("---")

    # 1️⃣ Data Handling
    st.markdown("<h4 style='text-align: center;'>1️⃣ Data Handling - <code>(kale.loaddata)</h4>", unsafe_allow_html=True)
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
    st.markdown("<h4 style='text-align: center;'>7️⃣ Pipeline - <code>(kale.evaluate)</h4>", unsafe_allow_html=True)
    st.write("---")

    # 📌 Full Example: Putting Everything Together
    st.markdown("<h4 style='text-align: center;'>📌 Full Example: Putting Everything Together</h4>", unsafe_allow_html=True)
    st.write("---")

    # 📌 Summary
    st.markdown("<h4 style='text-align: center;'>📌 Summary</h4>", unsafe_allow_html=True)
    st.write("---")

    # 📌 Next Step
    st.markdown("<h4 style='text-align: center;'>📌 Next Step</h4>", unsafe_allow_html=True)