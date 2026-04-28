from cumulative import cumulative_avg, cumulative_max


def test_cumulative_avg_basic():
    assert cumulative_avg([2, 4, 6]) == [2.0, 3.0, 4.0]


def test_cumulative_avg_single():
    assert cumulative_avg([10]) == [10.0]


def test_cumulative_max_basic():
    assert cumulative_max([3, 1, 4, 1, 5]) == [3.0, 3.0, 4.0, 4.0, 5.0]


def test_cumulative_max_empty():
    assert cumulative_max([]) == []
