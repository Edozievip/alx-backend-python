#!/usr/bin/env python3
'''Async Generator module
'''

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
	'''This coroutine loops 10*, waits for 1 sec and yields a random number between 0 and 10'''
	for _ in range(10):
		random = random.random() * 10
		await asyncio.sleep(1)
		yield random
	
