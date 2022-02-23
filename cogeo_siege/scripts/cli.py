"""cogeo_siege.scripts.cli: cogeo_siege CLI."""

import click
from rasterio.rio import options

from cogeo_siege import __version__
from cogeo_siege.siege import create_config


@click.command(short_help="cogeo_siege CLI")
@options.file_in_arg
@click.option(
    "--output",
    "-o",
    type=click.Path(exists=False),
    help="Output file name",
    required=True,
)
@click.option("--minzoom", type=int, help="Overide COG MinZoom.")
@click.option("--maxzoom", type=int, help="Overide COG MaxZoom.")
@click.option(
    "--quiet", "-q", help="Remove progressbar and other non-error output.", is_flag=True
)
@click.version_option(version=__version__, message="%(version)s")
def siege(input, output, minzoom, maxzoom, quiet):
    """cogeo_siege."""

    create_config(input, output, minzoom=minzoom, maxzoom=maxzoom, quiet=quiet)
