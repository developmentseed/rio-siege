"""rio_siege.scripts.cli: rio-siege CLI."""

import click
import morecantile
from rasterio.rio import options

from rio_siege import __version__
from rio_siege.siege import create_config


@click.command(short_help="rio-siege CLI")
@options.file_in_arg
@click.option(
    "--output",
    "-o",
    type=click.Path(exists=False),
    help="Output file name",
    required=True,
)
@click.option(
    "-n",
    "--number-of-url",
    type=int,
    help="Number of URL.",
    show_default=True,
    default=1000,
)
@click.option("--minzoom", type=int, help="Override Dataset MinZoom.")
@click.option("--maxzoom", type=int, help="Override Dataset MaxZoom.")
@click.option(
    "--tms",
    type=click.Choice(morecantile.tms.list()),
    help="Morecantile TMS.",
    show_default=True,
    default="WebMercatorQuad",
)
@click.option(
    "--quiet", "-q", help="Remove progressbar and other non-error output.", is_flag=True
)
@click.version_option(version=__version__, message="%(version)s")
def siege(input, output, number_of_url, minzoom, maxzoom, tms, quiet):
    """Create Siege configuration file from raster datasets."""
    create_config(
        input,
        output,
        tms=morecantile.tms.get(tms),
        minzoom=minzoom,
        maxzoom=maxzoom,
        max_url=number_of_url,
        quiet=quiet,
    )
