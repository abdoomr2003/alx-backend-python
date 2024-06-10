#!/usr/bin/env python3

"""
This script defines an asynchronous function to wait for a random delay.

The function `wait_random` waits for a random amount of time between 0 and
a specified maximum delay.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously waits for a random delay between 0 and max_delay seconds.

    Args:
        max_delay (int, optional): The maximum number of seconds to wait.
        Defaults to 10.

    Returns:
        float: The actual number of seconds waited.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
