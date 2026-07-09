import time
import streamlit as st

from services.auth_service import login_user


# ==========================================================
# LOGIN PAGE
# ==========================================================

def show_login():

    # ------------------------------------------------------
    # BRANDING
    # ------------------------------------------------------

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """
        <h1 style="text-align:center;">
            🚀 Tasklytics
        </h1>

        <p style="
            text-align:center;
            color:#9CA3AF;
            margin-bottom:40px;
        ">
            Where Productivity Meets Intelligence
        </p>
        """,
        unsafe_allow_html=True
    )

    # ------------------------------------------------------
    # CENTER CARD
    # ------------------------------------------------------

    left, center, right = st.columns([1, 2, 1])

    with center:

        card = st.container(border=True)

        with card:

            st.markdown(
    """
    <h2 style="
        text-align:center;
        margin-bottom:8px;
        font-weight:700;
    ">
        Welcome Back
    </h2>

    <p style="
        text-align:center;
        color:#9CA3AF;
        margin-bottom:28px;
        font-size:15px;
    ">
        Login to continue to Tasklytics.
    </p>
    """,
    unsafe_allow_html=True
)

            st.write("")

            email = st.text_input(
                "Email Address",
                placeholder="john@example.com"
            )

            password = st.text_input(
                "Password",
                type="password"
            )

            st.write("")

            form_valid = (

                email.strip() != ""

                and password.strip() != ""

            )
             # ==========================================
            # LOGIN BUTTON
            # ==========================================

            if st.button(
                "🚀 Login",
                use_container_width=True,
                disabled=not form_valid
            ):

                with st.spinner("Signing you in..."):

                    success, message, user = login_user(
                        email=email.strip().lower(),
                        password=password
                    )

                    time.sleep(1)

                if success:

                    st.success("🎉 Login Successful!")

                    time.sleep(1)

                    st.session_state.logged_in = True
                    st.session_state.user_id = user["user_id"]
                    st.session_state.user_name = user["name"]
                    st.session_state.current_page = "dashboard"

                    st.rerun()

                else:

                    st.error(message)

            st.divider()

            st.markdown(
                "<p style='text-align:center;'>Don't have an account?</p>",
                unsafe_allow_html=True
            )

            if st.button(
                "Create Account",
                use_container_width=True
            ):

                st.session_state.current_page = "register"

                st.rerun()

    st.markdown("<br><br>", unsafe_allow_html=True)