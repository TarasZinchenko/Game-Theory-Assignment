"""
Rock-Paper-Scissors (RPS) Game Logic, Strategy Solver, and Monte Carlo Simulation.
"""

from typing import Dict, Tuple, List, Any
import numpy as np


STANDARD_RPS_PAYOFFS: Dict[str, Dict[str, Tuple[int, int]]] = {
    'Rock': {'Rock': (0, 0), 'Paper': (-1, 1), 'Scissors': (1, -1)},
    'Paper': {'Rock': (1, -1), 'Paper': (0, 0), 'Scissors': (-1, 1)},
    'Scissors': {'Rock': (-1, 1), 'Paper': (1, -1), 'Scissors': (0, 0)}
}

MODIFIED_RPS_PAYOFFS: Dict[str, Dict[str, Tuple[int, int]]] = {
    'Rock': {'Rock': (0, 0), 'Paper': (-2, 2), 'Scissors': (1, -1)},
    'Paper': {'Rock': (2, -2), 'Paper': (0, 0), 'Scissors': (-1, 1)},
    'Scissors': {'Rock': (-1, 1), 'Paper': (1, -1), 'Scissors': (0, 0)}
}


def calculate_optimal_bot_strategy(
    payoff_matrix: Dict[str, Dict[str, Tuple[int, int]]]
) -> Dict[str, float]:
    """
    Calculate bot's optimal strategy given a payoff matrix.

    :param payoff_matrix: Nested dictionary mapping moves to payoffs (bot_payoff, opp_payoff)
    :return: Dictionary mapping move names to probabilities
    """
    moves = ['Rock', 'Paper', 'Scissors']
    opponent_strategy = {move: 1.0 / 3.0 for move in moves}

    expected_utilities = {
        move: sum(
            payoff_matrix[move][opp_move][0] * prob
            for opp_move, prob in opponent_strategy.items()
        )
        for move in moves
    }

    positive_eu = {move: max(eu, 0.0) for move, eu in expected_utilities.items()}
    total_eu = sum(positive_eu.values())

    if total_eu > 0:
        return {move: eu / total_eu for move, eu in positive_eu.items()}
    else:
        return {move: 1.0 / 3.0 for move in moves}


def run_rps_simulation(
    bot_strategy: Dict[str, float],
    audience_dist: Dict[str, float],
    n_trials: int = 100000
) -> Dict[str, Any]:
    """
    Run Monte Carlo simulation of RPS rounds.

    :param bot_strategy: Bot's choice probabilities
    :param audience_dist: Audience choice probabilities
    :param n_trials: Number of simulation rounds
    :return: Dictionary containing scores, cumulative scores, bot choices, and audience choices
    """
    moves = ['Rock', 'Paper', 'Scissors']
    bot_probs = [bot_strategy[m] for m in moves]
    aud_probs = [audience_dist[m] for m in moves]

    bot_choices = np.random.choice(moves, size=n_trials, p=bot_probs)
    audience_choices = np.random.choice(moves, size=n_trials, p=aud_probs)

    # Use standard payoff evaluation for scoring
    # Calculate scores directly
    score_map = {
        ('Rock', 'Rock'): 0, ('Rock', 'Paper'): -1, ('Rock', 'Scissors'): 1,
        ('Paper', 'Rock'): 1, ('Paper', 'Paper'): 0, ('Paper', 'Scissors'): -1,
        ('Scissors', 'Rock'): -1, ('Scissors', 'Paper'): 1, ('Scissors', 'Scissors'): 0,
    }

    scores = np.array([score_map[(b, a)] for b, a in zip(bot_choices, audience_choices)])
    cumulative_scores = np.cumsum(scores)

    return {
        "scores": scores,
        "total_score": int(np.sum(scores)),
        "cumulative_scores": cumulative_scores,
        "bot_choices": bot_choices,
        "audience_choices": audience_choices,
        "n_trials": n_trials
    }
