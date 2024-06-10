#!/usr/bin/env python3
"""
Module to measure the average time taken for executing multiple asynchronous
tasks.
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Measure the average time taken to complete n asynchronous tasks with
    a maximum delay.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay for each wait_random call.

    Returns:
        float: The average time taken for each of the n tasks.
    """
    delays = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)
    return delays
