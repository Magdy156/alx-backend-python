#!/usr/bin/env python3
"""Excutes  coroutines at the same time"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Returns list of all the delays random float"""
    delays: List[float] = []
    orderList: List[float] = []

    for i in range(n):
        delays.append(wait_random(max_delay))

    for j in asyncio.as_completed(delays):
        orderList.append(await j)

    return orderList
