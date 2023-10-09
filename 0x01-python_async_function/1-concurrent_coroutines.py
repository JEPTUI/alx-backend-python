#!/usr/bin/env python3
"""Imports wait_random from the previous python file
and writes async routine"""


import asyncio
from typing import List
from random import uniform
from asyncio import run, gather


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Takes in 2 int arguments and return
    the list of all the delays (float values)"""
    delays: List[float] = await gather(*(
        wait_random(max_delay) for _ in range(n)))
    delays.sort()
    return delays


if __name__ == "__main__":
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
