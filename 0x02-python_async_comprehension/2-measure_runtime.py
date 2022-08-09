#!/usr/bin/env python3
"""
coroutine that will execute async_comprehension four
times in parallel using asyncio.gather.
"""
import asyncio
import time

async_generator = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ retunr a list with ten random numbers  """
    initial_time = time.time()
    await asyncio.gather(
        async_generator(),
        async_generator(),
        async_generator(),
        async_generator()
    )
    final_time = time.time() - initial_time
    return final_time
