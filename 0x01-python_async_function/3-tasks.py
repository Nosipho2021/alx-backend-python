#!/usr/bin/env python3
import asyncio
from typing import Any
from 0-basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio Task for the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: An asyncio Task object for the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
