#!/usr/bin/env python3
"""
functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    return a function that multiplies a float
    """
    def multiplies(n: float):
        """
        multiply two numbers
        """
        return n * multiplier
    return multiplies
