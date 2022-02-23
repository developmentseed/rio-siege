"""cogeo_siege module."""

from setuptools import setup

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name="cogeo_siege",
    install_requires=["rio_tiler>=3.1,<4.0"],
    extras_require={
        "test": [
            "pytest",
            "pytest-cov",
        ],
        "dev": [
            "pytest",
            "pytest-cov",
            "pre-commit",
            "tox",
        ],
    },
)
