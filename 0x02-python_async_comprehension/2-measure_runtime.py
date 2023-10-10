#!/usr/bin/env python3
"""Defines a a measure_runtime coroutine"""


import asyncio
from typing import List
import time
import random


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def async_generator() -> float:
    await asyncio.sleep(1)
    return random.uniform(0, 10)


async def async_comprehension() -> List[float]:
    return [await async_generator() for _ in range(10)]


async def measure_runtime() -> float:
    start_time = time.time()
    await asyncio.gather(
            async_comprehension(), async_comprehension(),
            async_comprehension(), async_comprehension())
    end_time = time.time()
    return end_time - start_time
