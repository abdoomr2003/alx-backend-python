#!/usr/bin/env python3

"""
Module to create an asyncio Task for executing a coroutine with a specified
delay.
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio Task to run wait_random with the specified maximum delay.

    Args:
        max_delay (int): The maximum delay in seconds for the wait_random
        coroutine.

    Returns:
        asyncio.Task: An asyncio Task object for the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
