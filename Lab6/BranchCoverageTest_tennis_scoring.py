


import pytest
from tennis_scoring import game_score, set_winner, match_status


@pytest.mark.parametrize("a,b,expected", [
    (0, 0, "0-0"),
    (1, 2, "15-30"),
    (2, 1, "30-15"),
    (3, 3, "deuce"),
    (4, 4, "deuce"),
    (4, 3, "advantage A"),
    (3, 4, "advantage B"),
    (5, 3, "game A"),
    (3, 5, "game B"),
    (4, 0, "game A"),
    (0, 4, "game B"),
])
def test_game_score_branches(a, b, expected):
    assert game_score(a, b) == expected


@pytest.mark.parametrize("a,b", [
    (-1, 0),
    (0, -1),
])
def test_negative_points(a, b):
    with pytest.raises(ValueError):
        game_score(a, b)


@pytest.mark.parametrize("a,b,expected", [
    (6, 0, "A"),
    (6, 4, "A"),
    (0, 6, "B"),
    (4, 6, "B"),
    (7, 6, "A"),
    (6, 7, "B"),
    (6, 5, None),
    (5, 6, None),
    (3, 2, None),
])
def test_set_winner_branches(a, b, expected):
    assert set_winner(a, b) == expected


@pytest.mark.parametrize("a,b,best_of,expected", [
    (2, 0, 3, "A wins"),
    (0, 2, 3, "B wins"),
    (1, 1, 3, "decider"),
    (0, 0, 3, "in progress"),
])
def test_match_status_branches(a, b, best_of, expected):
    assert match_status(a, b, best_of) == expected
