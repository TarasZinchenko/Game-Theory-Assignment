"""
Penalty Kick Game Theory Logic and Strategy Solvers.
"""

from typing import List, Tuple, Dict, Any


MESSI_PRESET: Dict[str, float] = {
    "player_strategy_left": 0.398,
    "player_strategy_middle": 0.078,
    "player_strategy_right": 0.524,
    "accuracy_left": 0.756,
    "accuracy_middle": 0.875,
    "accuracy_right": 0.759,
}

RONALDO_PRESET: Dict[str, float] = {
    "player_strategy_left": 0.642,
    "player_strategy_middle": 0.114,
    "player_strategy_right": 0.244,
    "accuracy_left": 0.873,
    "accuracy_middle": 0.643,
    "accuracy_right": 0.867,
}

DEFAULT_PRESET: Dict[str, float] = {
    "player_strategy_left": 0.33,
    "player_strategy_middle": 0.34,
    "player_strategy_right": 0.33,
    "accuracy_left": 1.0,
    "accuracy_middle": 0.2,
    "accuracy_right": 0.5,
}


def calculate_optimal_kick_probabilities(x_effectiveness: float) -> Tuple[float, float]:
    """
    Calculate kicker's optimal probability to choose Left (p)
    and goalie's optimal probability to dive Left (q).

    :param x_effectiveness: Kicker's relative effectiveness when kicking right (float between 0 and 1)
    :return: Tuple of (p_kicker_left, q_goalie_left)
    """
    p = 1.0 / (1.0 + x_effectiveness)
    q = x_effectiveness / (1.0 + x_effectiveness)
    return p, q


def calculate_normalized_probabilities(
    player_strategy: List[float], accuracies: List[float]
) -> List[float]:
    """
    Calculate and normalize effective shot probabilities based on strategy distribution and accuracies.

    :param player_strategy: List of probabilities [left, middle, right]
    :param accuracies: List of accuracies [left, middle, right]
    :return: Normalized probabilities summing to 1.0
    """
    effective_probabilities = [p * acc for p, acc in zip(player_strategy, accuracies)]
    total = sum(effective_probabilities)
    if total == 0:
        return [1.0 / len(player_strategy)] * len(player_strategy)
    return [p / total for p in effective_probabilities]
