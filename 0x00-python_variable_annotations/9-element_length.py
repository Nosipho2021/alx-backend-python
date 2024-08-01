#!/usr/bin/env python3
"""
This module provides a function to get the length of elements in an iterable.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples where each tuple contains an element from the input iterable
    and the length of that element.

    Parameters:
    lst (Iterable[Sequence]): An iterable of sequences (e.g., lists, strings).

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples where each tuple contains a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
