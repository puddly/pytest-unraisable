import gc
import sys
import warnings
import contextlib
import test.support

import pytest


MAJOR_VERSION = 0
MINOR_VERSION = 0
PATCH_VERSION = 1

__short_version__ = f"{MAJOR_VERSION}.{MINOR_VERSION}"
__version__ = f"{__short_version__}.{PATCH_VERSION}"


@pytest.hookimpl(hookwrapper=True)
def pytest_pyfunc_call(pyfuncitem):
    if hasattr(sys, "unraisablehook"):
        catch_unraisable = test.support.catch_unraisable_exception()
    else:
        catch_unraisable = contextlib.nullcontext()

    with warnings.catch_warnings():
        warnings.simplefilter("error")

        with catch_unraisable as cm:
            yield 
            gc.collect()

            if cm.unraisable is not None:
                raise cm.unraisable.exc_value
