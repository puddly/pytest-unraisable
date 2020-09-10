import sys
import asyncio

import pytest


async def async_coro():
    await asyncio.sleep(0)


@pytest.mark.asyncio
async def test_coroutine_awaited():
    await async_coro()


@pytest.mark.xfail(reason="coroutine not awaited warning", strict=True)
@pytest.mark.skipif(sys.version_info < (3, 8), reason="requires python3.8 or higher")
@pytest.mark.asyncio
async def test_coroutine_not_awaited():
    async_coro()
