#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine that waits for a random delay.
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for  random delay between 0 and max_delay seconds and returns delay.

    Args:
        max_delay (int): The maximum delay in seconds (default is 10).

    Returns:
        float: The actual delay in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
