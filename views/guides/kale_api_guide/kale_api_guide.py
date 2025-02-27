import streamlit as st
from navigation import go_to


# def kale_api_page():
#     """The KALE API - Detailed Breakdown of how it works"""

#     st.markdown(
#         """
#         <div style="text-align:center;">
#             <h2>📌 The KALE API Guide</h2>
#             <p style="font-size:18px;">Explore the different modules in the PyKale API.</p>
#         </div>
#         """,
#         unsafe_allow_html=True
#     )
#     st.write("---")

#     # API Modules
#     modules = {
#         "Data Handling (loaddata)": "loaddata_page",
#         "Data Preprocessing (prepdata)": "prepdata_page",
#         "Feature Extraction (embed)": "embed_page",
#         "Model Prediction (predict)": "predict_page",
#         "Evaluation (evaluate)": "evaluate_page",
#         "Interpretation (interpret)": "interpret_page",
#         "Pipeline (pipeline)": "pipeline_page"
#     }

#     for name, nav in modules.items():
#         if st.button(name):
#             go_to(nav)

#     st.write("---")

#     # 📌 Next Steps
#     st.markdown(
#         """
#         <div style="text-align:center;">
#             <h3>🚀 Next Steps</h3>
#             <p>Learn more about PyKale and start implementing:</p>
#             <ul style="display: inline-block; text-align: left;">
#                 <li>📖 <a href="https://pykale.readthedocs.io/" target="_blank">PyKale Documentation</a></li>
#                 <li>🔬 <a href="https://github.com/pykale/pykale" target="_blank">GitHub Repository</a></li>
#                 <li>📊 <a href="" target="_self">Demo</a></li>
#             </ul>
#         </div>
#         """,
#         unsafe_allow_html=True
#     )

def kale_api_page():
    """The KALE API - Detailed Breakdown of how it works"""

    st.markdown(
        """
        <div style="text-align:center;">
            <h2>📌 The KALE API Guide</h2>
            <p style="font-size:18px;">Explore the different modules in the PyKale API.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.write("---")

    # API Modules
    modules = {
        "Data Handling (loaddata)": "loaddata_page",
        "Data Preprocessing (prepdata)": "prepdata_page",
        "Feature Extraction (embed)": "embed_page",
        "Model Prediction (predict)": "predict_page",
        "Evaluation (evaluate)": "evaluate_page",
        "Interpretation (interpret)": "interpret_page",
        "Pipeline (pipeline)": "pipeline_page"
    }

    for name, nav in modules.items():
        if st.button(name):
            go_to(nav)

    st.write("---")

    # 📌 Next Steps
    st.markdown(
        """
        <div style="text-align:center;">
            <h3>🚀 Next Steps</h3>
            <p>Learn more about PyKale and start implementing:</p>
            <ul style="display: inline-block; text-align: left;">
                <li>📖 <a href="https://pykale.readthedocs.io/" target="_blank">PyKale Documentation</a></li>
                <li>🔬 <a href="https://github.com/pykale/pykale" target="_blank">GitHub Repository</a></li>
                <li>📊 <a href="" target="_self">Demo</a></li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
