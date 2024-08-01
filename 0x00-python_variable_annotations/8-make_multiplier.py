#!/usr/bin/env python3
"""
This module provides a function to create a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a function that multiplies a given float by a specified multiplier.

    The function returned by `make_multiplier` takes a float as an argument and
    returns the result of multiplying that float by the `multiplier` provided when
    `make_multiplier` was called.

    Parameters:
    multiplier (float): The multiplier to use in the returned function.

    Returns:
    Callable[[float], float]: A function that takes a float and returns a float
    which is the product of the input float and the `multiplier`.
    """


    def multiplier_function(value: float) -> float:
        """
        Multiplies the given float value by the multiplier.

        Parameters:
        value (float): The float value to be multiplied.

        Returns:
        float: The result of multiplying `value` by the `multiplier`.
        """
        return value * multiplier
    
    return multiplier_function
