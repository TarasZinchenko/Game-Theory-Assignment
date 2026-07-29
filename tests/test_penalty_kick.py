"""
Unit tests for Penalty Kick game theory logic.
"""

import pytest
from game_theory.core.penalty_kick import (
    calculate_optimal_kick_probabilities,
    calculate_normalized_probabilities,
)


def test_calculate_optimal_kick_probabilities_equal():
    p, q = calculate_optimal_kick_probabilities(1.0)
    assert pytest.approx(p, 0.001) == 0.5
    assert pytest.approx(q, 0.001) == 0.5


def test_calculate_optimal_kick_probabilities_asymmetric():
    # If X = 0.5 (50% right-side effectiveness)
    p, q = calculate_optimal_kick_probabilities(0.5)
    assert pytest.approx(p, 0.001) == 1.0 / 1.5  # ~0.6667
    assert pytest.approx(q, 0.001) == 0.5 / 1.5  # ~0.3333


def test_calculate_normalized_probabilities():
    strategy = [0.5, 0.3, 0.2]
    accuracies = [1.0, 1.0, 1.0]
    norm_probs = calculate_normalized_probabilities(strategy, accuracies)
    assert pytest.approx(sum(norm_probs), 0.001) == 1.0
    assert norm_probs == pytest.approx([0.5, 0.3, 0.2], 0.001)


def test_calculate_normalized_probabilities_with_accuracies():
    strategy = [0.4, 0.4, 0.2]
    accuracies = [0.5, 1.0, 0.5]  # effective: 0.2, 0.4, 0.1 (total 0.7)
    norm_probs = calculate_normalized_probabilities(strategy, accuracies)
    assert pytest.approx(sum(norm_probs), 0.001) == 1.0
    assert norm_probs[1] > norm_probs[0]
