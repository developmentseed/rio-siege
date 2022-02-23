# cogeo-siege

<p align="center">
  <a href="https://github.com/developmentseed/cogeo-siege/actions?query=workflow%3ACI" target="_blank">
      <img src="https://github.com/developmentseed/cogeo-siege/workflows/CI/badge.svg" alt="Test">
  </a>
  <a href="https://codecov.io/gh/developmentseed/cogeo-siege" target="_blank">
      <img src="https://codecov.io/gh/developmentseed/cogeo-siege/branch/main/graph/badge.svg" alt="Coverage">
  </a>
  <a href="https://pypi.org/project/cogeo-siege" target="_blank">
      <img src="https://img.shields.io/pypi/v/cogeo-siege?color=%2334D058&label=pypi%20package" alt="Package version">
  </a>
  <a href="https://github.com/developmentseed/cogeo-siege/blob/main/LICENSE" target="_blank">
      <img src="https://img.shields.io/github/license/developmentseed/cogeo-siege.svg" alt="Downloads">
  </a>
</p>

---

**Documentation**:

**Source Code**: <a href="https://github.com/developmentseed/cogeo-siege" target="_blank">https://github.com/developmentseed/cogeo-siege</a>

---

## Description

Create [siege](https://github.com/JoeDog/siege) configuration files from Cloud Optimized GeoTIFF.

This project is mostly inspired from the great [TileSiege](https://github.com/bdon/TileSiege)



## Install

You can install `cogeo-siege` using pip

```bash
$ pip install -U pip
$ pip install -U cogeo-siege
```

or install from source:

```bash
$ git clone https://github.com/developmentseed/cogeo-siege.git
$ cd cogeo-siege
$ pip install -U pip
$ pip install -e .
```

## Usage

```
$ cogeo-siege --help
Usage: cogeo-siege [OPTIONS] INPUT

  Create Siege configuration file from COG.

Options:
  -o, --output PATH  Output file name  [required]
  --minzoom INTEGER  Overide COG MinZoom.
  --maxzoom INTEGER  Overide COG MaxZoom.
  -q, --quiet        Remove progressbar and other non-error output.
  --version          Show the version and exit.
  --help             Show this message and exit.
```

```
$ cogeo-siege my_cog.tif -o test.txt
 6 |   677 █████
 7 |   731 █████
 8 |   873 ██████
 9 |   998 ██████
10 |  1284 ████████
11 |  1265 ████████
12 |  1765 ███████████
13 |  2407 ███████████████

$ head test.txt
PROT=http
HOST=localhost
PORT=8080
PATH=my_cog.tif
EXT=pbf
$(PROT)://$(HOST):$(PORT)/$(PATH)6/35/22.$(EXT)
$(PROT)://$(HOST):$(PORT)/$(PATH)6/35/21.$(EXT)
$(PROT)://$(HOST):$(PORT)/$(PATH)6/34/22.$(EXT)
$(PROT)://$(HOST):$(PORT)/$(PATH)6/35/22.$(EXT)
$(PROT)://$(HOST):$(PORT)/$(PATH)6/33/22.$(EXT)
```

## Contribution & Development

See [CONTRIBUTING.md](https://github.com/developmentseed/cogeo-siege/blob/main/CONTRIBUTING.md)

## Authors

Created by [Development Seed](<http://developmentseed.org>)

See [contributors](https://github.com/developmentseed/cogeo-siege/graphs/contributors) for a listing of individual contributors.

## License

See [LICENSE](https://github.com/developmentseed/cogeo-siege/blob/main/LICENSE)
