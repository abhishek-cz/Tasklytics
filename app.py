import streamlit as st


from pages.auth.login import show_login
from pages.auth.register import show_register

from utils.ui import load_css

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Tasklytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

load_css()


# ==========================================================
# SESSION STATE INITIALIZATION
# ==========================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user_id" not in st.session_state:
    st.session_state.user_id = None

if "user_name" not in st.session_state:
    st.session_state.user_name = None

if "current_page" not in st.session_state:
    st.session_state.current_page = "login"


# ==========================================================
# DASHBOARD PLACEHOLDER
# ==========================================================

def show_dashboard():

    st.title(f"👋 Welcome, {st.session_state.user_name}")

    st.success("Authentication Successful!")

    st.write("Tasklytics Dashboard will be built in the next milestone.")

    st.write("")

    col1, col2 = st.columns([1, 5])

    with col1:

        if st.button(
            "🚪 Logout",
            use_container_width=True
        ):

            st.session_state.logged_in = False
            st.session_state.user_id = None
            st.session_state.user_name = None
            st.session_state.current_page = "login"

            st.rerun()


# ==========================================================
# ROUTER
# ==========================================================

if st.session_state.logged_in:

    show_dashboard()

else:

    if st.session_state.current_page == "login":

        show_login()

    elif st.session_state.current_page == "register":

        show_register()