import sys

# Needed to fix enviroment errors on streamlit cloud. 
try:
    import pysqlite3
    sys.modules["sqlite3"] = sys.modules.pop("pysqlite3")
except ImportError:
    pass

import streamlit as st
from navigation import navbar
from views.guides.kale_api_guide.embed_page import embed_page
from views.guides.kale_api_guide.evaluate_page import evaluate_page
from views.guides.kale_api_guide.interpret_page import interpret_page
from views.guides.kale_api_guide.loaddata_page import loaddata_page
from views.guides.kale_api_guide.pipeline_page import pipeline_page
from views.guides.kale_api_guide.predict_page import predict_page
from views.guides.kale_api_guide.prepdata_page import prepdata_page
from views.home_page import home_page
from views.hub import hub_page
from views.demos.video_demo import video_demo_page
from views.demos.domain_adaptation_demo import domain_adaptation_page
from views.guides.introduction_guide import introduction_page
from views.guides.kale_api_guide.kale_api_guide import kale_api_page
from views.chatbot_page import chatbot_page

def main():    
    st.set_page_config(layout="wide")  

    if "page" not in st.session_state:
        st.session_state["page"] = "home"

    navbar()

    # Page routing
    if st.session_state["page"] == "home":
        home_page()
    elif st.session_state["page"] == "hub":
        hub_page()
    elif st.session_state["page"] == "video_example":
        video_demo_page()
    elif st.session_state["page"] == "domain_adaptation":
        domain_adaptation_page()
    elif st.session_state["page"] == "introduction":
        introduction_page()
    elif st.session_state["page"] == "kale_api":
        kale_api_page()
    elif st.session_state["page"] == "chatbot_page":
        chatbot_page()
    elif st.session_state["page"] == "loaddata_page":
        loaddata_page()
    elif st.session_state["page"] == "prepdata_page":
        prepdata_page()
    elif st.session_state["page"] == "embed_page":
        embed_page()
    elif st.session_state["page"] == "predict_page":
        predict_page()
    elif st.session_state["page"] == "evaluate_page":
        evaluate_page()
    elif st.session_state["page"] == "interpret_page":
        interpret_page()
    elif st.session_state["page"] == "pipeline_page":
        pipeline_page()


if __name__ == "__main__":
    main()