#!/usr/bin/env pyhon3
"""Adding type annotations to the function"""
from typing import Union, Any, Mapping, TypeVar


T = TypeVar('T')


def safely_get_value(
        dct: Mapping, key: Any, default: Union[T, None] = None
        ) -> Union[Any, T]:
    """Safely get a value from a dictionary, with an optional default value"""
    if key in dct:
        return dct[key]
    else:
        return default
