#!/usr/bin/env python3
"""Defines an asynchronous coroutine that takes in an integer
argument"""


import asyncio
import random


async def wait_random(max_delay=10):
    """Takes in an integer argument
    (max_delay, with a default value of 10)"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

async def main():
    max_delay = 5
    result = await wait_random(max_delay)
    print(f"Waited for {result:.2f} seconds")

asyncio.run(main())
