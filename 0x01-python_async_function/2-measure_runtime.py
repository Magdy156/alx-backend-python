#!/usr/bin/env python3
"""Measures the total execution time"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Returns the total time / n"""
    start = time.perf_counter()  # returns the float value of time in seconds
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    return (end - start) / n
