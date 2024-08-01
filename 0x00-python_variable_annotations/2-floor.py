#!/usr/bin/env python3
"""
This module provides a function to compute the floor of a floating point number.
"""

import math


def floor(n: float) -> int:
    """
    Computes the floor of a floating point number.

    This function uses the `math.floor` method to return the largest integer
    less than or equal to the given floating-point number.

    Parameters:
    n (float): The floating-point number whose floor is to be computed.

    Returns:
    int: The largest integer less than or equal to `n`.
    """
    return math.floor(n)
