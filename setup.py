"""cogeo_siege module."""
import sys

from setuptools import setup

sys.stderr.write(
    """
===============================
Unsupported installation method
===============================
cogeo-siege no longer supports installation with `python setup.py install`.
Please use `python -m pip install .` instead.
"""
)
sys.exit(1)


# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name="cogeo-siege",
    install_requires=["rio_tiler>=4.0.0a0,<5.0"],
    extras_require={
        "test": [
            "pytest",
            "pytest-cov",
        ],
        "dev": [
            "pre-commit",
        ],
    },
)
