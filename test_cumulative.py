"""
test_cumulative.py – unit tests for cumulative.py

Regression test for issue #1 is in TestCumulativeAvgEmptyInput.
"""

import unittest
from cumulative import cumulative_avg, cumulative_sum


class TestCumulativeAvg(unittest.TestCase):
    """Existing behavioural tests."""

    def test_single_element(self):
        self.assertEqual(cumulative_avg([4]), [4.0])

    def test_multiple_elements(self):
        self.assertEqual(cumulative_avg([1, 2, 3]), [1.0, 1.5, 2.0])

    def test_floats(self):
        result = cumulative_avg([0.5, 1.5])
        self.assertAlmostEqual(result[0], 0.5)
        self.assertAlmostEqual(result[1], 1.0)

    def test_negative_values(self):
        result = cumulative_avg([-2, -4])
        self.assertAlmostEqual(result[0], -2.0)
        self.assertAlmostEqual(result[1], -3.0)

    def test_length_preserved(self):
        data = list(range(1, 6))
        self.assertEqual(len(cumulative_avg(data)), len(data))


class TestCumulativeAvgEmptyInput(unittest.TestCase):
    """
    Regression tests for issue #1:
    'off-by-one in cumulative_avg overflows on empty input'

    BEFORE fix
    ----------
    $ python -m pytest test_cumulative.py::TestCumulativeAvgEmptyInput -v
    FAILED test_cumulative.py::TestCumulativeAvgEmptyInput::test_empty_input
    - IndexError: list index out of range

    AFTER fix
    ---------
    $ python -m pytest test_cumulative.py::TestCumulativeAvgEmptyInput -v
    PASSED test_cumulative.py::TestCumulativeAvgEmptyInput::test_empty_input
    """

    def test_empty_input_returns_empty_list(self):
        """cumulative_avg([]) must return [] — not raise IndexError."""
        # On unfixed code this raises: IndexError: list index out of range
        result = cumulative_avg([])
        self.assertEqual(result, [],
                         "cumulative_avg([]) should return [] but got: "
                         f"{result!r}")

    def test_empty_input_type(self):
        """Return value for empty input must be a list."""
        result = cumulative_avg([])
        self.assertIsInstance(result, list)

    def test_empty_input_length(self):
        """Return value for empty input must have length 0."""
        result = cumulative_avg([])
        self.assertEqual(len(result), 0)


class TestCumulativeSum(unittest.TestCase):
    """Tests for cumulative_sum helper."""

    def test_empty(self):
        self.assertEqual(cumulative_sum([]), [])

    def test_single(self):
        self.assertEqual(cumulative_sum([7]), [7])

    def test_multiple(self):
        self.assertEqual(cumulative_sum([1, 2, 3]), [1, 3, 6])


if __name__ == "__main__":
    unittest.main()
