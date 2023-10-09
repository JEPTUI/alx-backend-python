#!/usr/bin/env python3
"""Defines a function to create a measure_time"""


import asyncio
import time
from typing import List


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Takes integers n and max_delay as arguments that measures the total
    execution time for wait_n(n, max_delay), and returns total_time / n"""
    total_time = 0.0

    for _ in range(n):
        start_time = time.time()
        asyncio.run(wait_n(1, max_delay))
        end_time = time.time()
        total_time += (end_time - start_time)
    avrge_time = total_time / n

    return avrge_time


if __name__ == "__main__":
    n = 5
    max_delay = 9
    result = measure_time(n, max_delay)
    print(result)
