"""
Unit tests for Rock-Paper-Scissors strategy solvers and simulation engine.
"""

import pytest
from game_theory.core.rps import (
    STANDARD_RPS_PAYOFFS,
    calculate_optimal_bot_strategy,
    run_rps_simulation,
)


def test_standard_rps_optimal_strategy():
    strategy = calculate_optimal_bot_strategy(STANDARD_RPS_PAYOFFS)
    assert pytest.approx(strategy['Rock'], 0.001) == 1.0 / 3.0
    assert pytest.approx(strategy['Paper'], 0.001) == 1.0 / 3.0
    assert pytest.approx(strategy['Scissors'], 0.001) == 1.0 / 3.0


def test_run_rps_simulation():
    bot_strat = {'Rock': 0.33, 'Paper': 0.33, 'Scissors': 0.34}
    aud_dist = {'Rock': 0.33, 'Paper': 0.33, 'Scissors': 0.34}
    n_trials = 1000

    sim = run_rps_simulation(bot_strat, aud_dist, n_trials=n_trials)
    assert len(sim['scores']) == n_trials
    assert len(sim['cumulative_scores']) == n_trials
    assert sim['n_trials'] == n_trials
