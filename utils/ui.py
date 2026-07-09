import streamlit as st
from datetime import datetime


# ==========================================================
# Load Global CSS
# ==========================================================

def load_css():

    with open("assets/styles/main.css") as css:

        st.markdown(
            f"<style>{css.read()}</style>",
            unsafe_allow_html=True
        )


# ==========================================================
# Dynamic Greeting
# ==========================================================

def dashboard_header(user_name):

    hour = datetime.now().hour

    if hour < 12:

        greeting = "🌅 Good Morning"

        quote = "Win the morning. Win the day."

    elif hour < 17:

        greeting = "☀️ Good Afternoon"

        quote = "Stay consistent. Results will follow."

    elif hour < 21:

        greeting = "🌇 Good Evening"

        quote = "Small progress every day adds up."

    else:

        greeting = "🌙 Good Night"

        quote = "Plan today. Conquer tomorrow."

    st.markdown(
        f"""
        <h1>{greeting}, {user_name}</h1>
        <p style='font-size:18px;color:#A7B0C0;margin-top:-8px;'>
            {quote}
        </p>
        """,
        unsafe_allow_html=True
    )


# ==========================================================
# Section Title
# ==========================================================

def section_title(title):

    st.markdown(
        f"""
        <h2 style='margin-top:35px;margin-bottom:18px;'>
            {title}
        </h2>
        """,
        unsafe_allow_html=True
    )


# ==========================================================
# Glass Card
# ==========================================================

def glass_card(title, content):

    st.markdown(
        f"""
        <div class="metric-card">
            <h3 style="margin:0;color:white;">
                {title}
            </h3>

            <p style="margin-top:10px;">
                {content}
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


# ==========================================================
# Metric Card
# ==========================================================

def metric_card(icon, title, value):

    st.markdown(
        f"""
        <div class="metric-card">

            <div style="
                font-size:30px;
                margin-bottom:10px;
            ">
                {icon}
            </div>

            <div style="
                color:#A7B0C0;
                font-size:14px;
            ">
                {title}
            </div>

            <div style="
                color:white;
                font-size:34px;
                font-weight:700;
                margin-top:8px;
            ">
                {value}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )