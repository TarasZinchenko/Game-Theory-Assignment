"""
Take vs. Share Strategic Dilemma Logic.
"""

from typing import Tuple


def calculate_take_share_payoffs(q_opponent_takes: float) -> Tuple[float, float]:
    """
    Calculate expected payoffs for Player 1 taking vs sharing given Player 2's take probability q.

    :param q_opponent_takes: Probability that Player 2 chooses 'Take' (0.0 to 1.0)
    :return: Tuple (expected_payoff_take, expected_payoff_share)
    """
    e_take = 8000.0 * (1.0 - q_opponent_takes)
    e_share = 4000.0 * (1.0 - q_opponent_takes)
    return e_take, e_share
