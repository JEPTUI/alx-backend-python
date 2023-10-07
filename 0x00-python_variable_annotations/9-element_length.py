#!/usr/bin/python3
"""Annotate the below function parameters"""
from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Calculates the length of each element in the input iterable
    and return values with the appropriate types"""
    return [(i, len(i)) for i in lst]
