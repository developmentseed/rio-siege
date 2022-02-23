"""cogeo_siege.siege create urls."""

import math
import random
from typing import Any, Dict, Optional

import click
import morecantile
from rio_tiler.io import COGReader


def _percentage_split(size, percentages: Dict[int, float]):
    """Freely copied from TileSiege https://github.com/bdon/TileSiege"""
    prv = 0
    cumsum = 0.0
    for zoom, p in percentages.items():
        cumsum += p
        nxt = int(cumsum * size)
        yield zoom, prv, nxt
        prv = nxt


def create_config(
    source: str,
    output: str,
    minzoom: Optional[int] = None,
    maxzoom: Optional[int] = None,
    tms: Optional[morecantile.TileMatrixSet] = None,
    max_url: int = 10000,
    quiet: bool = False,
) -> None:
    """Create siege config.

    This is mostly adapted from the excellent TileSiege https://github.com/bdon/TileSiege
    """
    tms = tms or morecantile.tms.get("WebMercatorQuad")

    with COGReader(source, tms=tms) as cog:
        info = cog.info()

        minzoom = minzoom if minzoom is not None else info.minzoom
        maxzoom = maxzoom if maxzoom is not None else info.maxzoom
        w, s, e, n = info.bounds

        # Truncate BBox to the TMS bounds
        w = max(tms.bbox.left, w)
        s = max(tms.bbox.bottom, s)
        e = min(tms.bbox.right, e)
        n = min(tms.bbox.top, n)

        random.seed(3857)

        distribution = [
            2,
            2,
            6,
            12,
            16,
            27,
            38,
            41,
            49,
            56,
            72,
            71,
            99,
            135,
            135,
            136,
            102,
            66,
            37,
            6,
        ]  # the total distribution...

        total_weight = 0
        extremas: Dict[int, Any] = {}
        for zoom in range(minzoom, maxzoom + 1):
            total_weight = total_weight + distribution[zoom]
            ul_tile = tms.tile(w, n, zoom)
            lr_tile = tms.tile(e, s, zoom)
            extremas[zoom] = {
                "x": {"min": ul_tile.x, "max": lr_tile.x + 1},
                "y": {"min": ul_tile.y, "max": lr_tile.y + 1},
            }

        with open(output, "w") as f:
            f.write("PROT=http\n")
            f.write("HOST=localhost\n")
            f.write("PORT=8080\n")
            f.write(f"PATH={source}\n")
            f.write("EXT=pbf\n")
            rows = 0
            for zoom, start, end in _percentage_split(
                max_url,
                {
                    zoom: distribution[zoom] / total_weight
                    for zoom in range(minzoom, maxzoom + 1)
                },
            ):
                extrema = extremas[zoom]
                rows_for_zoom = end - start
                rows += rows_for_zoom
                for sample in range(rows_for_zoom):
                    x = random.randint(extrema["x"]["min"], extrema["x"]["max"])
                    y = random.randint(extrema["y"]["min"], extrema["y"]["max"])
                    f.write(f"$(PROT)://$(HOST):$(PORT)/$(PATH){zoom}/{x}/{y}.$(EXT)\n")

                if not quiet:
                    p1 = " " if zoom < 10 else ""
                    p2 = " " * (len(str(10000)) - len(str(rows_for_zoom)))
                    bar = "█" * math.ceil(rows_for_zoom / max_url * 60)
                    click.echo(f"{p1}{zoom} | {p2}{rows_for_zoom} {bar}", err=True)
