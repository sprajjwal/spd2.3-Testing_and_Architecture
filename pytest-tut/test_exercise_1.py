# test_exercise_1.py

import math

def get_average(li):
    if len(li) == 0:
        return float('NaN')
    sum = 0
    for num in li:
        sum += num
    mean = sum / len(li)
    return mean


def test_get_average_expected_inputs():
    # all pos
    assert get_average([1, 3, 5, 7]) == 4
    # pos integers and floats
    assert get_average([0.5, 2, 2.5, 3.5]) == 2.25
    # pos floats
    assert get_average([1.2, 1.4]) == 1.3
    # pos and neg ints
    assert get_average([-1, -2, 1, 2]) == 0
    # pos, neg, ints, and floating points
    

def test_get_average_empty_list():
    assert math.isnan(get_average([]))