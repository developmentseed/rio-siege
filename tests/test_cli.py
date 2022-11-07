"""test rio-siege cli."""

import os
from unittest.mock import patch

from click.testing import CliRunner

from rio_siege.scripts.cli import siege

cog_path = os.path.join(os.path.dirname(__file__), "fixtures", "cog.tif")


def test_siege_version():
    """Should work as expected."""
    runner = CliRunner()
    result = runner.invoke(siege, ["--version"])
    assert not result.exception
    assert result.exit_code == 0


def test_siege():
    """Should work as expected."""
    runner = CliRunner()

    with runner.isolated_filesystem():
        result = runner.invoke(siege, [cog_path, "-o", "tmp.txt"])
        assert not result.exception
        assert result.exit_code == 0

        result = runner.invoke(siege, [cog_path, "-o", "tmp.txt", "--minzoom", 8])
        assert not result.exception
        assert result.exit_code == 0
