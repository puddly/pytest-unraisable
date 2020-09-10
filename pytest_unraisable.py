import gc
import sys
import warnings
import contextlib

import pytest


MAJOR_VERSION = 0
MINOR_VERSION = 0
PATCH_VERSION = 1

__short_version__ = f"{MAJOR_VERSION}.{MINOR_VERSION}"
__version__ = f"{__short_version__}.{PATCH_VERSION}"


# Copied from the Python-internal `test.support.catch_unraisable_exception`
class catch_unraisable_exception:
    def __init__(self):
        self.unraisable = None
        self._old_hook = None

    def _hook(self, unraisable):
        # Storing unraisable.object can resurrect an object which is being
        # finalized. Storing unraisable.exc_value creates a reference cycle.
        self.unraisable = unraisable

    def __enter__(self):
        self._old_hook = sys.unraisablehook
        sys.unraisablehook = self._hook
        return self

    def __exit__(self, *exc_info):
        sys.unraisablehook = self._old_hook
        del self.unraisable


@pytest.hookimpl(hookwrapper=True)
def pytest_pyfunc_call(pyfuncitem):
    if hasattr(sys, "unraisablehook"):
        catch_unraisable = catch_unraisable_exception()
    else:
        catch_unraisable = contextlib.nullcontext()

    with warnings.catch_warnings():
        warnings.simplefilter("error")

        with catch_unraisable as cm:
            yield 
            gc.collect()

            if cm.unraisable is not None:
                raise cm.unraisable.exc_value
