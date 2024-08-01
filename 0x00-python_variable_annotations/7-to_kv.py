#!/usr/bin/env python3
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Converts a string and a number to a tuple with the string and the square of the number.

    Parameters:
    k (str): A string value.
    v (Union[int, float]): An integer or float value.

    Returns:
    Tuple[str, float]: A tuple where the first element is the string k, and the second element is the square of v as a float.
    """
    return (k, float(v ** 2))
