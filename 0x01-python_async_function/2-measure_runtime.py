#!/usr/bin/env python3
''' Description: Create a measure_time function with integers n and
                 max_delay as arguments that measures the total execution
                 time for wait_n(n, max_delay), and returns total_time / n.
                 Your function should return a float.
'''

from time import time
from asyncio import run

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    ''' Return execution time for wait_n given `n` and `max_delay`. '''
    initial_time = time()
    run(wait_n(n, max_delay))
    final_time = time()
    elapsed_time = final_time - initial_time
    return elapsed_time / n
