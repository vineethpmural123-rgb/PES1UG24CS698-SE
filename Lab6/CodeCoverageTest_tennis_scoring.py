
import pytest
from tennis_scoring import game_score, set_winner, match_status


# Game score tests
def test_game_start():
    assert game_score(0, 0) == "0-0"


def test_regular_scores():
    assert game_score(1, 2) == "15-30"
    assert game_score(2, 1) == "30-15"


def test_negative_points():
    with pytest.raises(ValueError):
        game_score(-1, 0)
    with pytest.raises(ValueError):
        game_score(0, -1)


def test_deuce():
    assert game_score(3, 3) == "deuce"
    assert game_score(4, 4) == "deuce"


def test_advantage():
    assert game_score(4, 3) == "advantage A"
    assert game_score(3, 4) == "advantage B"


def test_game_winners():
    assert game_score(5, 3) == "game A"
    assert game_score(3, 5) == "game B"
    assert game_score(4, 0) == "game A"
    assert game_score(0, 4) == "game B"


# Set winner tests
def test_set_winners():
    assert set_winner(6, 0) == "A"
    assert set_winner(0, 6) == "B"
    assert set_winner(7, 6) == "A"
    assert set_winner(6, 7) == "B"
    assert set_winner(3, 2) is None


def test_set_requires_two_game_lead():
    assert set_winner(6, 5) is None
    assert set_winner(5, 6) is None


# Match status tests
def test_match_a_wins():
    assert match_status(2, 0, 3) == "A wins"


def test_match_b_wins():
    assert match_status(0, 2, 3) == "B wins"


def test_match_decider():
    assert match_status(1, 1, 3) == "decider"


def test_match_in_progress():
    assert match_status(0, 0, 3) == "in progress"
