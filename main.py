import sys

# Needed to fix enviroment errors on streamlit cloud. 
try:
    import pysqlite3
    sys.modules["sqlite3"] = sys.modules.pop("pysqlite3")
except ImportError:
    pass

import streamlit as st
from navigation import navbar
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


if __name__ == "__main__":
    main()