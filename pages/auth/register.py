import re
import time
import streamlit as st

from services.auth_service import register_user


# ==========================================================
# EMAIL VALIDATION
# ==========================================================

EMAIL_PATTERN = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"


def is_valid_email(email):
    return re.match(EMAIL_PATTERN, email)


# ==========================================================
# PASSWORD STRENGTH
# ==========================================================

def password_strength(password):

    checks = {

        "length": len(password) >= 8,

        "uppercase": any(c.isupper() for c in password),

        "lowercase": any(c.islower() for c in password),

        "number": any(c.isdigit() for c in password),

        "special": any(not c.isalnum() for c in password)

    }

    score = sum(checks.values())

    if score <= 2:

        label = "Weak"
        color = "red"

    elif score <= 4:

        label = "Medium"
        color = "orange"

    else:

        label = "Strong"
        color = "green"

    return score, label, color, checks


# ==========================================================
# REGISTER PAGE
# ==========================================================

def show_register():

    # -----------------------------
    # TOP BRANDING
    # -----------------------------

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

    # -----------------------------
    # CENTER PAGE
    # -----------------------------

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
        Create Account
    </h2>

    <p style="
        text-align:center;
        color:#9CA3AF;
        margin-bottom:28px;
        font-size:15px;
    ">
        Join thousands of productive users.
    </p>
    """,
    unsafe_allow_html=True
)

            st.write("")

            name = st.text_input(
                "Full Name",
                placeholder="John Doe"
            )

            email = st.text_input(
                "Email Address",
                placeholder="john@example.com"
            )

            password = st.text_input(
                "Password",
                type="password"
            )

            confirm_password = st.text_input(
                "Confirm Password",
                type="password"
            )

            email_valid = False

            if email:

                if is_valid_email(email):

                    st.success("✅ Valid email")

                    email_valid = True

                else:

                    st.error("❌ Invalid email")

            score = 0

            checks = {}

            if password:

                score, label, color, checks = password_strength(password)

                st.progress(score * 20)

                st.markdown(
                    f"**Password Strength:** :{color}[{label}]"
                )

                st.write(
                    f"{'✅' if checks['length'] else '❌'} Minimum 8 characters"
                )

                st.write(
                    f"{'✅' if checks['uppercase'] else '❌'} One uppercase letter"
                )

                st.write(
                    f"{'✅' if checks['lowercase'] else '❌'} One lowercase letter"
                )

                st.write(
                    f"{'✅' if checks['number'] else '❌'} One number"
                )

                st.write(
                    f"{'✅' if checks['special'] else '❌'} One special character"
                )
                st.write("")

            # ==========================================
            # CONFIRM PASSWORD
            # ==========================================

            password_match = False

            if confirm_password:

                if password == confirm_password:

                    password_match = True

                    st.success("✅ Passwords match")

                else:

                    st.error("❌ Passwords do not match")

            # ==========================================
            # FORM VALIDATION
            # ==========================================

            form_valid = (

                name.strip() != ""

                and email_valid

                and password_match

                and score == 5

            )

            st.write("")

            # ==========================================
            # CREATE ACCOUNT BUTTON
            # ==========================================

            if st.button(

                "🚀 Create Account",

                use_container_width=True,

                disabled=not form_valid

            ):

                with st.spinner("Creating your account..."):

                    success, message = register_user(

                        name=name.strip(),

                        email=email.strip().lower(),

                        password=password

                    )

                    time.sleep(1)

                if success:

                    st.success("🎉 Account created successfully!")

                    st.balloons()

                    time.sleep(1)

                    st.session_state.current_page = "login"

                    st.rerun()

                else:

                    st.error(message)

            st.divider()

            st.markdown(
                "<p style='text-align:center;'>Already have an account?</p>",
                unsafe_allow_html=True
            )

            if st.button(

                "Login",

                use_container_width=True

            ):

                st.session_state.current_page = "login"

                st.rerun()

    st.markdown("<br><br>", unsafe_allow_html=True)