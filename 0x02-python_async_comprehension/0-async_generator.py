#!/usr/bin/env python3
"""
DESCRIPTION:
Write a coroutine called async_generator that takes no arguments.

The coroutine will loop 10 times, each time asynchronously wait
1 second, then yield a random number between 0 and 10. Use the
random module.
"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ generates 10 random numbers between 0 and 10"""
    wait: int = 1
    for i in range(0, 10, 1):
        await asyncio.sleep(wait)
        yield random.random() * 10
