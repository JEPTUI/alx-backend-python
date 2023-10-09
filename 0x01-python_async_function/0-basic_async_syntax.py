#!/usr/bin/env python3
"""Defines an asynchronous coroutine that takes in an integer
argument"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Takes in an integer argument
    (max_delay, with a default value of 10)"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


if __name__ == "__main__":
    asyncio.run(wait_random())
    asyncio.run(wait_random(5))
    asyncio.run(wait_random(15))
