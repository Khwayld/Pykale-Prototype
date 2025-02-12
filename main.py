import streamlit as st
from navigation import navbar
from views.home_page import home_page
from views.archive_page import archive_page
from views.video_demo_page.video_main import video_demo_page
from views.domain_adaptation_page.domain_main import domain_adaptation_page




def main():    
    st.set_page_config(layout="wide")  

    if "page" not in st.session_state:
        st.session_state["page"] = "home"

    navbar()

    # Page routing
    if st.session_state["page"] == "home":
        home_page()
    elif st.session_state["page"] == "archive":
        archive_page()
    elif st.session_state["page"] == "video_example":
        video_demo_page()
    elif st.session_state["page"] == "domain_adaptation":
        domain_adaptation_page()



if __name__ == "__main__":
    main()