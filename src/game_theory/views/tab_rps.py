"""
Rock-Paper-Scissors Analyzer Tab View.
"""

import streamlit as st
import pandas as pd
import numpy as np
from game_theory.core.rps import (
    STANDARD_RPS_PAYOFFS,
    MODIFIED_RPS_PAYOFFS,
    calculate_optimal_bot_strategy,
    run_rps_simulation,
)
from game_theory.utils.charts import (
    build_rps_score_progression_chart,
    build_rps_choice_distribution_chart,
)


def render_tab_rps() -> None:
    st.header("Advanced Rock-Paper-Scissors Analyzer")

    st.sidebar.header("⚖️ RPS Configuration")
    payoff_mode = st.sidebar.radio(
        "Preset Modes",
        ('Standard RPS', 'Modified RPS', 'Custom'),
        help="Standard: Classic RPS rules\nModified: Adjusted payoffs\nCustom: Full control"
    )

    if payoff_mode == 'Standard RPS':
        payoff_matrix = STANDARD_RPS_PAYOFFS
    elif payoff_mode == 'Modified RPS':
        payoff_matrix = MODIFIED_RPS_PAYOFFS
    else:
        st.sidebar.subheader("Custom Payoffs")
        payoff_matrix = {}
        moves = ['Rock', 'Paper', 'Scissors']
        for move in moves:
            payoff_matrix[move] = {}
            for opp_move in moves:
                bot_payoff = st.sidebar.number_input(
                    f'{move} vs {opp_move} (Bot payoff)',
                    min_value=-10,
                    max_value=10,
                    value=0
                )
                opp_payoff = -bot_payoff
                payoff_matrix[move][opp_move] = (bot_payoff, opp_payoff)

    st.subheader("Current Payoff Matrix (Bot, Opponent)")
    display_matrix = pd.DataFrame({
        move: {opp_move: f"({payoff_matrix[move][opp_move][0]}, {payoff_matrix[move][opp_move][1]})"
               for opp_move in payoff_matrix[move]}
        for move in payoff_matrix
    }).T
    st.dataframe(display_matrix)

    st.sidebar.header("🤖 Bot Strategy")
    bot_strategy_mode = st.sidebar.radio(
        "Strategy Mode",
        ('Optimal', 'Fixed R:25% P:25% S:50%'),
        help="Select the bot's strategy"
    )

    if bot_strategy_mode == 'Optimal':
        bot_strategy = calculate_optimal_bot_strategy(payoff_matrix)
    else:
        bot_strategy = {'Rock': 0.25, 'Paper': 0.25, 'Scissors': 0.50}

    st.subheader("Bot's Strategy Distribution")
    strategy_df = pd.DataFrame.from_dict(bot_strategy, orient='index', columns=['Probability'])
    st.table(strategy_df.style.format("{:.2%}"))

    st.sidebar.header("🎲 Simulation Settings")
    sim_mode = st.sidebar.radio(
        "Simulation Mode",
        ('Manual Input', 'Random Trials'),
        help="Choose audience input method"
    )

    if sim_mode == 'Manual Input':
        st.sidebar.subheader("Audience Distribution")
        rock = st.sidebar.number_input("Rock Choices", 0, 100000, 0)
        paper = st.sidebar.number_input("Paper Choices", 0, 100000, 100000)
        scissors = st.sidebar.number_input("Scissors Choices", 0, 100000, 0)
        total = rock + paper + scissors
        audience_dist = {
            'Rock': rock / total if total > 0 else 0.33,
            'Paper': paper / total if total > 0 else 0.33,
            'Scissors': scissors / total if total > 0 else 0.33
        }
    else:
        n_trials_input = st.sidebar.selectbox("Number of Trials", [100, 1000, 10000, 100000], index=2)
        if st.sidebar.button("Generate Random Trials"):
            generated_probs = np.random.dirichlet(np.ones(3), size=1)[0]
            audience_dist = dict(zip(['Rock', 'Paper', 'Scissors'], generated_probs))
        else:
            audience_dist = {'Rock': 0.33, 'Paper': 0.33, 'Scissors': 0.34}

    if st.sidebar.button("Run Simulation"):
        st.subheader("Simulation Results")
        sim_results = run_rps_simulation(bot_strategy, audience_dist, n_trials=100000)

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total Score (Bot)", f"{sim_results['total_score']:+,}")
            fig_cum = build_rps_score_progression_chart(
                sim_results['n_trials'], sim_results['cumulative_scores']
            )
            st.plotly_chart(fig_cum, use_container_width=True)

        with col2:
            fig_dist = build_rps_choice_distribution_chart(
                sim_results['bot_choices'], sim_results['audience_choices']
            )
            st.plotly_chart(fig_dist, use_container_width=True)
