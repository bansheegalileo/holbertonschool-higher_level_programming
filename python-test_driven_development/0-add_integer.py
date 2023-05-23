#!/usr/bin/python3
"""
Add Integer or Float Module
"""


def add_integer(a, b=98):
    """
    add 2 ints

    Args:
        a (int/float): int 1
        b (int/float): int 2

    Raises:
        TypeError: if not int or float

    Return:
        (int) : sum of a  and b
    """
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    if (a + b) == float('inf') or (a + b) == -float('inf'):
        return b
    return int(a) + int(b)
