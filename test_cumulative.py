"""test_cumulative.py – unit tests for cumulative.py"""

import pytest
from cumulative import cumulative_avg


# ---------------------------------------------------------------------------
# Regression test for issue #1
# "off-by-one in cumulative_avg overflows on empty input"
#
# BEFORE fix:
#   >>> cumulative_avg([])
#   Traceback (most recent call last):
#     ...
#   IndexError: list index out of range
#
# AFTER fix:
#   >>> cumulative_avg([])
#   []
# ---------------------------------------------------------------------------
def test_cumulative_avg_empty_input():
    """cumulative_avg([]) must return [] without raising (regression: issue #1)."""
    result = cumulative_avg([])
    assert result == [], f"Expected [], got {result!r}"


# ---------------------------------------------------------------------------
# Normal-operation tests
# ---------------------------------------------------------------------------

def test_cumulative_avg_single_element():
    assert cumulative_avg([4]) == [4.0]


def test_cumulative_avg_multiple_elements():
    result = cumulative_avg([1, 2, 3])
    assert result == [1.0, 1.5, 2.0]


def test_cumulative_avg_length_matches_input():
    data = [10, 20, 30, 40]
    result = cumulative_avg(data)
    assert len(result) == len(data)


def test_cumulative_avg_running_values():
    result = cumulative_avg([2, 4, 6])
    # avg after idx 0: 2/1=2.0
    # avg after idx 1: (2+4)/2=3.0
    # avg after idx 2: (2+4+6)/3=4.0
    assert result == [2.0, 3.0, 4.0]


def test_cumulative_avg_floats():
    result = cumulative_avg([1.5, 2.5])
    assert result[0] == pytest.approx(1.5)
    assert result[1] == pytest.approx(2.0)


def test_cumulative_avg_negative_numbers():
    result = cumulative_avg([-4, -2])
    assert result[0] == pytest.approx(-4.0)
    assert result[1] == pytest.approx(-3.0)
