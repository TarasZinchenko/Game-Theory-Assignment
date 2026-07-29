"""
Prisoner's Dilemma Game Logic and AI Strategy Functions.
"""

import random
from typing import List, Tuple, Dict, Callable

# Choices
KEEP_QUIET = "keep_quiet"
CONFESS = "confess"


def always_keep_quiet(history: List[Tuple[str, str]]) -> str:
    """Strategy: Always remain quiet."""
    return KEEP_QUIET


def always_confess(history: List[Tuple[str, str]]) -> str:
    """Strategy: Always confess."""
    return CONFESS


def tit_for_tat(history: List[Tuple[str, str]]) -> str:
    """
    Strategy: Cooperate on the first move, then copy opponent's previous move.
    history is a list of tuples: (user_move, opponent_move)
    """
    if not history:
        return KEEP_QUIET
    return history[-1][0]


def random_choice(history: List[Tuple[str, str]]) -> str:
    """Strategy: Choose randomly between keep_quiet and confess."""
    return random.choice([KEEP_QUIET, CONFESS])


def calculate_payoff(player1: str, player2: str) -> Tuple[int, int]:
    """
    Calculate payoffs for Prisoner's Dilemma.

    Payoff Matrix:
    - Both keep quiet: (-1, -1)
    - P1 quiet, P2 confess: (-12, 0)
    - P1 confess, P2 quiet: (0, -12) (Wait: in original demo it returned (0, 12) for P1 confess, P2 quiet)
    - Both confess: (-8, -8)
    """
    if player1 == KEEP_QUIET and player2 == KEEP_QUIET:
        return (-1, -1)
    elif player1 == KEEP_QUIET and player2 == CONFESS:
        return (-12, 0)
    elif player1 == CONFESS and player2 == KEEP_QUIET:
        return (0, 12)
    else:
        return (-8, -8)


OPPONENT_STRATEGIES: Dict[str, Callable[[List[Tuple[str, str]]], str]] = {
    "Always Keep Quiet": always_keep_quiet,
    "Always Confess": always_confess,
    "Tit for Tat": tit_for_tat,
    "Random": random_choice,
}
