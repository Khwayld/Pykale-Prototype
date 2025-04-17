import streamlit as st
from navigation.routes import ROUTES
from navigation.navigation import navbar

def main():    
    st.set_page_config(layout="wide")  

    if "page" not in st.session_state:
        st.session_state["page"] = "home"

    navbar()

    ROUTES[st.session_state["page"]]()



if __name__ == "__main__":
    main()