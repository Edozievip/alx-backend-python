#!/usr/bin/env python3
'''Async Generator module.
'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''This loops 10*, waits a sec yields a random number between 0 and 10.
    '''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
