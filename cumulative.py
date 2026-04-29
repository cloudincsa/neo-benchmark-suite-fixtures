"""cumulative.py – running-average helpers for the benchmark suite."""


def cumulative_avg(numbers):
    """Return a list where element i is the average of numbers[0..i].

    Args:
        numbers: A list of numeric values.

    Returns:
        A list of floats the same length as *numbers*, or an empty list
        when *numbers* is empty.

    Raises:
        TypeError: if *numbers* contains non-numeric values.

    Examples:
        >>> cumulative_avg([])
        []
        >>> cumulative_avg([4])
        [4.0]
        >>> cumulative_avg([1, 2, 3])
        [1.0, 1.5, 2.0]
    """
    # --- FIX for issue #1 ---------------------------------------------------
    # Guard against empty input before any index arithmetic.  Without this
    # early return, the loop below would attempt numbers[0] on an empty list
    # and raise IndexError (off-by-one overflow on empty input).
    if not numbers:
        return []
    # ------------------------------------------------------------------------

    result = []
    running_sum = 0
    for i, value in enumerate(numbers):
        running_sum += value
        result.append(running_sum / (i + 1))
    return result
