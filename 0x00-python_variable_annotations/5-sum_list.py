#!/usr/bin/env python3
"""
This module provides a function to compute the sum of a list of floats.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Computes the sum of a list of floating point numbers.

    The function takes a list of floats and returns their sum. The sum is computed
    using the built-in `sum` function, which returns a float representing the sum of 
    all the elements in the input list.

    Parameters:
    input_list (List[float]): A list containing floating point numbers to be summed.

    Returns:
    float: The sum of the floating point numbers in the list.
    """
    return sum(input_list)
