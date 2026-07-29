"""
Unit tests for Prisoner's Dilemma strategies and payoff calculations.
"""

from game_theory.core.prisoners_dilemma import (
    calculate_payoff,
    tit_for_tat,
    always_confess,
    always_keep_quiet,
    KEEP_QUIET,
    CONFESS,
)


def test_calculate_payoff():
    assert calculate_payoff(KEEP_QUIET, KEEP_QUIET) == (-1, -1)
    assert calculate_payoff(KEEP_QUIET, CONFESS) == (-12, 0)
    assert calculate_payoff(CONFESS, KEEP_QUIET) == (0, 12)
    assert calculate_payoff(CONFESS, CONFESS) == (-8, -8)


def test_tit_for_tat_initial_move():
    history = []
    assert tit_for_tat(history) == KEEP_QUIET


def test_tit_for_tat_copies_opponent():
    history_user_confessed = [(CONFESS, KEEP_QUIET)]
    assert tit_for_tat(history_user_confessed) == CONFESS

    history_user_quiet = [(KEEP_QUIET, CONFESS)]
    assert tit_for_tat(history_user_quiet) == KEEP_QUIET


def test_always_strategies():
    history = [(KEEP_QUIET, KEEP_QUIET)]
    assert always_keep_quiet(history) == KEEP_QUIET
    assert always_confess(history) == CONFESS
