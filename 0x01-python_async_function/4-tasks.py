#!/usr/bin/env python3
"""Tasks Module"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Returns List of random float delays """
    delays: List[float] = []
    orderList: List[float] = []

    for i in range(n):
        delays.append(task_wait_random(max_delay))

    for o in asyncio.as_completed(delays):
        orderList.append(await o)

    return orderList
