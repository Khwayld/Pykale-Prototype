import streamlit as st
from pages import home_page, video_demo_page, domain_adaptation_page
from example_functions.video_loading_streamlit_example import demo_1





def main():    
    # init
    if "page" not in st.session_state:
        st.session_state["page"] = "home"

    # state management
    if st.session_state["page"] == "home":
        home_page()
    elif st.session_state["page"] == "video_example":
        video_demo_page()
    elif st.session_state["page"] == "domain_adaptation":
        domain_adaptation_page()



if __name__ == "__main__":
    main()