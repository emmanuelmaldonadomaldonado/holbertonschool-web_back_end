#!/usr/bin/env python3
"""Let's execute multiple coroutines 
at the same time with async
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int = 10, max_delay: int = 10):
    """FUNCTION"""
    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return sorted(delays)
