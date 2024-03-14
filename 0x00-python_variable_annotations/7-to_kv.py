#!/usr/bin/env python3
"""
to tuple func
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    to tuple
    """
    return (k, v**2)
