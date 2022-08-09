#!/usr/bin/env python3
"""
asynchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10) named wait_random
that waits for a random delay between 0 and max_delay
(included and float value) seconds and eventually returns it.
"""

import ramdom
import asyncio


def wait_ramdom(max_delay: int = 10) -> float:
    """ wait for a ramdom time and returns the waiting time"""
    wait = max_delay * ramdom.ramdom()
    await asyncio.sleep(wait)
    return wait
