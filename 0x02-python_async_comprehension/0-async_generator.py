#!/usr/bin/env python3

"""
Module to demonstrate an asynchronous generator that yields random float values
"""

from typing import AsyncGenerator
import asyncio
import random


async def async_generator() -> AsyncGenerator[float, None]:
    """
    An asynchronous generator that yields random float values between 0 and 1.

    Yields:
        float: A random float value between 0 and 1.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 1)
