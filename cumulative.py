"""cumulative.py – running-average helpers for the benchmark suite."""


def cumulative_avg(nums):
    """Return a list where element i is the average of nums[0..i].

    Args:
        nums: A list of real numbers.

    Returns:
        A list of the same length containing the cumulative averages,
        or an empty list if *nums* is empty.

    Examples:
        >>> cumulative_avg([])
        []
        >>> cumulative_avg([4])
        [4.0]
        >>> cumulative_avg([1, 2, 3])
        [1.0, 1.5, 2.0]
    """
    # --- FIX for issue #1 -------------------------------------------
    # The original code performed index arithmetic that assumed the list
    # was non-empty; calling cumulative_avg([]) raised
    #   IndexError: list index out of range
    # Return early with an empty list to satisfy the documented contract.
    if not nums:
        return []
    # ----------------------------------------------------------------

    result = []
    running_sum = 0
    for i, value in enumerate(nums):
        running_sum += value
        result.append(running_sum / (i + 1))
    return result
