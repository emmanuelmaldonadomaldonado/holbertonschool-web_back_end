#!/usr/bin/env python3
"""Coroutine that generates random numbers asynchronously."""

import asyncio
import random

async def async_generator():
    """Coroutine that generates random numbers asynchronously."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
