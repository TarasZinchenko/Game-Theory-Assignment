"""
Prisoner's Dilemma Tab View.
"""

import streamlit as st
import pandas as pd
from game_theory.core.prisoners_dilemma import (
    OPPONENT_STRATEGIES,
    calculate_payoff,
    KEEP_QUIET,
    CONFESS,
)


def render_tab_prisoners() -> None:
    st.header("Prisoner's Dilemma Simulation")

    col1, col2 = st.columns([2, 1])

    if "user_score" not in st.session_state:
        st.session_state.user_score = 0
        st.session_state.opponent_score = 0
        st.session_state.history = []

    with col1:
        opponent_name = st.selectbox("Choose an opponent:", list(OPPONENT_STRATEGIES.keys()))
        opponent_func = OPPONENT_STRATEGIES[opponent_name]

        col_btn1, col_btn2 = st.columns(2)

        if col_btn1.button("Keep Quiet", key="keep_quiet", use_container_width=True):
            user_move = KEEP_QUIET
            opponent_move = opponent_func(st.session_state.history)
            user_points, opp_points = calculate_payoff(user_move, opponent_move)
            st.session_state.user_score += user_points
            st.session_state.opponent_score += opp_points
            st.session_state.history.append((user_move, opponent_move))

        if col_btn2.button("Confess", key="confess", use_container_width=True):
            user_move = CONFESS
            opponent_move = opponent_func(st.session_state.history)
            user_points, opp_points = calculate_payoff(user_move, opponent_move)
            st.session_state.user_score += user_points
            st.session_state.opponent_score += opp_points
            st.session_state.history.append((user_move, opponent_move))

    with col2:
        st.subheader("Score & Payoff Matrix")
        st.metric(label="Your Score", value=st.session_state.user_score)
        st.metric(label="Opponent Score", value=st.session_state.opponent_score)

        payoff_matrix = pd.DataFrame({
            "You Keep Quiet": ["(-1,-1)", "(-12,0)"],
            "You Confess": ["(0,12)", "(-8,-8)"]
        }, index=["Opp. Keep Quiet", "Opp. Confess"])
        st.table(payoff_matrix)
