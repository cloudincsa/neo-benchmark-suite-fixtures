"""
cumulative.py – running/cumulative average utilities.

Fix (issue #1): cumulative_avg([]) now returns [] instead of raising
IndexError caused by an off-by-one that read nums[0] unconditionally
before checking whether the list was non-empty.
"""


def cumulative_avg(nums):
    """Return a list where element i is the average of nums[0..i].

    Args:
        nums: A list of numeric values.

    Returns:
        A list of floats the same length as *nums*, or [] if *nums* is empty.

    Raises:
        TypeError: if *nums* contains non-numeric values.

    Examples:
        >>> cumulative_avg([])
        []
        >>> cumulative_avg([4])
        [4.0]
        >>> cumulative_avg([1, 2, 3])
        [1.0, 1.5, 2.0]
    """
    # --- FIX for issue #1 -------------------------------------------
    # Guard against empty input BEFORE any element access so that the
    # off-by-one (reading nums[0] unconditionally) can never fire.
    if not nums:
        return []
    # ----------------------------------------------------------------

    result = []
    running_sum = 0
    for i, val in enumerate(nums):
        running_sum += val
        result.append(running_sum / (i + 1))
    return result


def cumulative_sum(nums):
    """Return a list where element i is the sum of nums[0..i].

    Args:
        nums: A list of numeric values.

    Returns:
        A list the same length as *nums*, or [] if *nums* is empty.
    """
    if not nums:
        return []
    result = []
    running = 0
    for val in nums:
        running += val
        result.append(running)
    return result
