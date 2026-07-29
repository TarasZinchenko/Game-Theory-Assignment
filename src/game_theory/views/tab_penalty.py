"""
Penalty Kick Analyzer Tab View.
"""

import streamlit as st
from game_theory.core.penalty_kick import (
    calculate_optimal_kick_probabilities,
    calculate_normalized_probabilities,
    MESSI_PRESET,
    RONALDO_PRESET,
    DEFAULT_PRESET,
)
from game_theory.utils.charts import build_penalty_strategy_chart
from game_theory.utils.goal_drawing import draw_color_coded_goal


def render_tab_penalty() -> None:
    st.title("Penalty Kick Analyzer")

    x_percent = st.slider(
        'Kicker’s effectiveness when kicking right (X%)',
        0, 100, 50, 1,
        key="penalty_slider"
    )
    x_val = x_percent / 100.0
    p, q = calculate_optimal_kick_probabilities(x_val)

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Kicker's optimal probability to choose Left", f"{p * 100:.1f}%")
    with col2:
        st.metric("Goalie's optimal probability to dive Left", f"{q * 100:.1f}%")

    fig1 = build_penalty_strategy_chart()
    st.plotly_chart(fig1, use_container_width=True)

    with st.expander("Why this counterintuitive result?"):
        st.markdown("""
        - **Higher right-side skill (X↑)**: Goalie anticipates this and dives right more often.  
        - **Paradoxical solution**: To exploit the goalie's bias, you must kick left **more frequently** than intuition suggests!
        """)

    col1, col2 = st.columns([1, 1])

    preset_messi = False
    preset_ronaldo = False

    with col1:
        if st.button("Messi"):
            preset_messi = True
    with col2:
        if st.button("Ronaldo"):
            preset_ronaldo = True

    if preset_messi:
        values = MESSI_PRESET
    elif preset_ronaldo:
        values = RONALDO_PRESET
    else:
        values = DEFAULT_PRESET

    player_strategy_left = st.slider(
        "Probability for Left", 0.0, 1.0, values["player_strategy_left"]
    )
    player_strategy_middle = st.slider(
        "Probability for Middle", 0.0, 1.0, values["player_strategy_middle"]
    )
    player_strategy_right = st.slider(
        "Probability for Right", 0.0, 1.0, values["player_strategy_right"]
    )
    accuracy_left = st.slider(
        "Accuracy for Left", 0.0, 1.0, values["accuracy_left"]
    )
    accuracy_middle = st.slider(
        "Accuracy for Middle", 0.0, 1.0, values["accuracy_middle"]
    )
    accuracy_right = st.slider(
        "Accuracy for Right", 0.0, 1.0, values["accuracy_right"]
    )

    player_strategy = [player_strategy_left, player_strategy_middle, player_strategy_right]
    accuracies = [accuracy_left, accuracy_middle, accuracy_right]

    normalized_probabilities = calculate_normalized_probabilities(player_strategy, accuracies)
    fig2 = draw_color_coded_goal(normalized_probabilities)
    st.pyplot(fig2)
