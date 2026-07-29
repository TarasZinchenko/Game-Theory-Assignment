"""
Plotly Chart Builders for Game Theory Suite.
"""

from typing import Dict, Any
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


def build_penalty_strategy_chart() -> go.Figure:
    """Build line chart of kicker's optimal left probability vs effectiveness."""
    x_percent_values = np.linspace(0, 100, 100)
    x_values = x_percent_values / 100.0
    p_values = 1.0 / (1.0 + x_values)

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=x_percent_values,
            y=p_values * 100,
            mode='lines',
            line=dict(color='purple', width=3)
        )
    )
    fig.update_layout(
        title="Optimal Kick Strategy vs Effectiveness",
        xaxis_title="X (% Effectiveness When Kicking Right)",
        yaxis_title="Probability to Choose Left (%)",
        height=500
    )
    return fig


def build_take_share_chart() -> go.Figure:
    """Build line chart of Expected Payoffs vs Opponent's Strategy (q)."""
    q_axis = np.linspace(0, 1, 100)
    e_take = 8000 * (1 - q_axis)
    e_share = 4000 * (1 - q_axis)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=q_axis, y=e_take, name='Take', line=dict(color='red')))
    fig.add_trace(go.Scatter(x=q_axis, y=e_share, name='Share', line=dict(color='blue')))
    fig.add_shape(
        type="rect",
        x0=0, x1=1, y0=4000, y1=8000,
        fillcolor="rgba(255,182,193,0.3)",
        line_width=0
    )
    fig.update_layout(
        title="Expected Payoffs vs Opponent's Strategy",
        xaxis_title="Probability Player 2 Takes (q)",
        yaxis_title="Expected Payoff",
        height=500
    )
    return fig


def build_rps_score_progression_chart(
    n_trials: int, cumulative_scores: np.ndarray
) -> go.Figure:
    """Build Plotly line chart for RPS cumulative score progression."""
    fig = px.line(
        x=range(n_trials),
        y=cumulative_scores,
        labels={'x': 'Trial', 'y': 'Cumulative Score'},
        title="Score Progression"
    )
    return fig


def build_rps_choice_distribution_chart(
    bot_choices: np.ndarray, audience_choices: np.ndarray
) -> go.Figure:
    """Build Plotly grouped bar chart for RPS choice frequency distribution."""
    dist_df = pd.DataFrame({
        'Bot': pd.Series(bot_choices).value_counts(normalize=True),
        'Audience': pd.Series(audience_choices).value_counts(normalize=True)
    })
    fig = px.bar(
        dist_df,
        barmode='group',
        labels={'value': 'Frequency', 'variable': 'Player'},
        title="Choice Distribution"
    )
    return fig
