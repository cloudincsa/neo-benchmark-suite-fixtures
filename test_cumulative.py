"""Tests for cumulative.py."""
import pytest
from cumulative import cumulative_avg


# ---------------------------------------------------------------------------
# Existing tests
# ---------------------------------------------------------------------------

def test_single_element():
    assert cumulative_avg([4]) == [4.0]


def test_multiple_elements():
    assert cumulative_avg([1, 2, 3]) == [1.0, 1.5, 2.0]


def test_all_same():
    assert cumulative_avg([5, 5, 5, 5]) == [5.0, 5.0, 5.0, 5.0]


# ---------------------------------------------------------------------------
# NEW test – regression for issue #1
# "off-by-one in cumulative_avg overflows on empty input"
#
# BEFORE fix: cumulative_avg([]) raised IndexError
# AFTER  fix: cumulative_avg([]) returns []
# ---------------------------------------------------------------------------

def test_empty_input():
    """cumulative_avg of an empty list must return [] without raising."""
    result = cumulative_avg([])
    assert result == [], (
        f"Expected [] for empty input, got {result!r}"
    )
