import pathlib
import pytest_unraisable

from setuptools import setup

setup(
    name="pytest-unraisable",
    version=pytest_unraisable.__version__,
    description="py.test module to capture unraisable exceptions",
    long_description=(pathlib.Path(__file__).parent / "README.md").read_text(),
    long_description_content_type="text/markdown",
    author="puddly",
    author_email="puddly3@gmail.com",
    url="https://github.com/puddly/pytest-unraisable/",
    license="GPLv3",
    py_modules=["pytest_unraisable"],
    entry_points={"pytest11": ["unraisable = pytest_unraisable"]},
    install_requires=["pytest>=2.7.0"],
    classifiers=["Framework :: Pytest"],
)
