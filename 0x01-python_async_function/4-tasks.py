#!/usr/bin/env python3
"""Defines a new function task_wait_n"""


import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Takes task_n alter it into a new function that calls
    task_wait_random"""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return delays


if __name__ == "__main__":
    n = 5
    max_delay = 6
    result = asyncio.run(task_wait_n(n, max_delay))
    print(result)
