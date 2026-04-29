"""cumulative.py — running-average utilities for neo-benchmark-suite-fixtures."""


def cumulative_avg(nums):
    """Return a list where element i is the average of nums[0..i].

    Returns an empty list when *nums* is empty.

    Fix for issue #1: the original code accessed nums[0] unconditionally,
    raising ``IndexError`` on an empty sequence.  We now return early so
    that ``cumulative_avg([]) == []``.
    """
    if not nums:          # ← fix: guard against empty input
        return []

    result = []
    running_sum = 0
    for i, value in enumerate(nums, start=1):
        running_sum += value
        result.append(running_sum / i)
    return result


def cumulative_sum(nums):
    """Return a list where element i is the sum of nums[0..i]."""
    result = []
    running = 0
    for value in nums:
        running += value
        result.append(running)
    return result
