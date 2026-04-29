"""test_cumulative.py — unit tests for cumulative.py."""

import pytest
from cumulative import cumulative_avg, cumulative_sum


# ---------------------------------------------------------------------------
# cumulative_avg — existing tests
# ---------------------------------------------------------------------------

class TestCumulativeAvg:
    def test_single_element(self):
        assert cumulative_avg([4]) == [4.0]

    def test_two_elements(self):
        assert cumulative_avg([1, 3]) == [1.0, 2.0]

    def test_multiple_elements(self):
        result = cumulative_avg([2, 4, 6])
        assert result == pytest.approx([2.0, 3.0, 4.0])

    def test_negative_numbers(self):
        result = cumulative_avg([-3, -1, 2])
        assert result == pytest.approx([-3.0, -2.0, -2 / 3])

    def test_floats(self):
        result = cumulative_avg([0.5, 1.5])
        assert result == pytest.approx([0.5, 1.0])

    # -----------------------------------------------------------------------
    # NEW TEST — issue #1: cumulative_avg([]) must return [], not raise
    # -----------------------------------------------------------------------
    def test_empty_input_returns_empty_list(self):
        """cumulative_avg([]) should return [] (issue #1 regression test).

        BEFORE fix:
            >>> cumulative_avg([])
            IndexError: list index out of range

        AFTER fix:
            >>> cumulative_avg([])
            []
        """
        result = cumulative_avg([])
        assert result == [], (
            f"Expected [], got {result!r}. "
            "Empty input must return an empty list, not raise IndexError."
        )


# ---------------------------------------------------------------------------
# cumulative_sum — existing tests
# ---------------------------------------------------------------------------

class TestCumulativeSum:
    def test_empty(self):
        assert cumulative_sum([]) == []

    def test_single_element(self):
        assert cumulative_sum([7]) == [7]

    def test_multiple_elements(self):
        assert cumulative_sum([1, 2, 3]) == [1, 3, 6]

    def test_negative_numbers(self):
        assert cumulative_sum([-1, -2, -3]) == [-1, -3, -6]
