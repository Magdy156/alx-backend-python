#!/usr/bin/env python3
"""
length ele func
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    length of element
    """
    return [(i, len(i)) for i in lst]
