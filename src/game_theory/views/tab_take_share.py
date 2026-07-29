"""
Take vs. Share Dilemma Tab View.
"""

import streamlit as st
from game_theory.core.take_share import calculate_take_share_payoffs
from game_theory.utils.charts import build_take_share_chart


def render_tab_take_share() -> None:
    st.header("Take vs. Share Strategic Analysis")

    q = st.slider(
        "Player 2's probability of Taking (q)",
        min_value=0.0,
        max_value=1.0,
        value=0.5,
        step=0.01,
        key="take_share_slider"
    )

    e_take, e_share = calculate_take_share_payoffs(q)

    fig2 = build_take_share_chart()

    col3, col4 = st.columns([1, 2])
    with col3:
        st.metric("Expected Payoff for Taking", f"${e_take:,.0f}")
        st.metric("Expected Payoff for Sharing", f"${e_share:,.0f}")
        st.error("**Take always dominates!**")

    with col4:
        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("""
    #### Payoff Matrix
    |                | Player 2: Take | Player 2: Share |
    |----------------|----------------|-----------------|
    | **Player 1: Take**  | (0, 0)        | (8000, 0)       |
    | **Player 1: Share** | (0, 8000)     | (4000, 4000)    |
    """)
