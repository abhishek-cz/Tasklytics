import streamlit as st

from utils.ui import (
    dashboard_header,
    metric_card,
    section_title,
    glass_card
)


def show_dashboard():

    # ==========================================
    # Header
    # ==========================================

    dashboard_header(st.session_state.user_name)

    st.write("")

    # ==========================================
    # Metric Cards
    # ==========================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        metric_card(
            "⚡",
            "XP",
            "0"
        )

    with col2:
        metric_card(
            "🏆",
            "Level",
            "1"
        )

    with col3:
        metric_card(
            "🔥",
            "Streak",
            "0"
        )

    with col4:
        metric_card(
            "📈",
            "Productivity",
            "0%"
        )

    st.write("")
    st.write("")

    # ==========================================
    # Tasks & Progress
    # ==========================================

    left, right = st.columns([2, 1])

    with left:

        section_title("📋 Today's Tasks")

        glass_card(
            "No Tasks Yet",
            "Click the Add Task button to begin your productivity journey."
        )

    with right:

        section_title("💡 Insight")

        glass_card(
            "Today's Tip",
            "Consistency beats intensity. Complete one important task before anything else."
        )

    st.write("")
    st.write("")

    # ==========================================
    # Weekly Progress
    # ==========================================

    section_title("📈 Weekly Progress")

    st.info("Interactive Plotly chart coming in the next milestone.")

    st.write("")
    st.write("")

    # ==========================================
    # Logout
    # ==========================================

    if st.button(
        "🚪 Logout",
        use_container_width=True
    ):

        st.session_state.logged_in = False
        st.session_state.user_id = None
        st.session_state.user_name = None
        st.session_state.current_page = "login"

        st.rerun()