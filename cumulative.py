"""Cumulative-stats utilities used by the analytics pipeline.

The bug: cumulative_avg crashes on an empty input list (IndexError) instead
of returning [] cleanly. The fix is a single-line guard at the top.
"""
from __future__ import annotations


def cumulative_avg(values: list[float]) -> list[float]:
    """Return the running mean of a list. cumulative_avg([]) should be [].

    >>> cumulative_avg([2, 4, 6])
    [2.0, 3.0, 4.0]
    >>> cumulative_avg([10])
    [10.0]
    """
    out = [float(values[0])]
    running = out[0]
    for i in range(1, len(values)):
        running += values[i]
        out.append(running / (i + 1))
    return out


def cumulative_max(values: list[float]) -> list[float]:
    """Running max. Handles empty list correctly."""
    if not values:
        return []
    out = [float(values[0])]
    for v in values[1:]:
        out.append(max(out[-1], float(v)))
    return out
