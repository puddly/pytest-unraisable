import sys
import asyncio
import warnings

import pytest


async def async_coro():
    await asyncio.sleep(0)


@pytest.mark.asyncio
async def test_coroutine_awaited():
    await async_coro()


@pytest.mark.xfail(reason="coroutine not awaited warning", strict=True)
@pytest.mark.skipif(sys.version_info < (3, 8), reason="requires python3.8 or higher")
@pytest.mark.catch_unraisable
@pytest.mark.asyncio
async def test_coroutine_not_awaited():
    async_coro()


@pytest.mark.xfail(reason="captured warnings should fail", strict=True)
@pytest.mark.filterwarnings("error")
def test_filtered_warnings():
    warnings.warn(UserWarning("test"))


def test_ignored_warnings():
    warnings.warn(UserWarning("test"))
