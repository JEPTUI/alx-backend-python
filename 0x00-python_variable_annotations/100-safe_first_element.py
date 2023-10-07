#!/usr/bin/env python3
"""Defines a code that is to be augmented
with correct duck-typed annotations"""
from typing import Union, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Removes the first element of an Iterable or
    return none if empty"""
    if lst:
        return lst[0]
    else:
        return None
