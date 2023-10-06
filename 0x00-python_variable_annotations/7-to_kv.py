#!/usr/bin/env python3
"""Defines a type-annotated function to_kv"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Takes a string k and an int OR float v as arguments and
    returns a tuple"""
    square = v ** 2
    return k, float(square)
