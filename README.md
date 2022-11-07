# rio-siege

<p align="center">
  <a href="https://github.com/developmentseed/rio-siege/actions?query=workflow%3ACI" target="_blank">
      <img src="https://github.com/developmentseed/rio-siege/workflows/CI/badge.svg" alt="Test">
  </a>
  <a href="https://codecov.io/gh/developmentseed/rio-siege" target="_blank">
      <img src="https://codecov.io/gh/developmentseed/rio-siege/branch/main/graph/badge.svg" alt="Coverage">
  </a>
  <a href="https://pypi.org/project/rio-siege" target="_blank">
      <img src="https://img.shields.io/pypi/v/rio-siege?color=%2334D058&label=pypi%20package" alt="Package version">
  </a>
  <a href="https://github.com/developmentseed/rio-siege/blob/main/LICENSE" target="_blank">
      <img src="https://img.shields.io/github/license/developmentseed/rio-siege.svg" alt="Downloads">
  </a>
</p>

---

**Documentation**:

**Source Code**: <a href="https://github.com/developmentseed/rio-siege" target="_blank">https://github.com/developmentseed/rio-siege</a>

---

## Description

Create [siege](https://github.com/JoeDog/siege) configuration files from Raster datasets.

This project is mostly inspired from the great [TileSiege](https://github.com/bdon/TileSiege)

## Install

You can install `rio-siege` using pip

```bash
$ pip install -U pip
$ pip install -U rio-siege
```

or install from source:

```bash
$ git clone https://github.com/developmentseed/rio-siege.git
$ cd rio-siege
$ pip install -U pip
$ pip install -e .
```

## Usage

```
$ rio siege --help
Usage: rio siege [OPTIONS] INPUT

  Create Siege configuration file from raster datasets.

Options:
  -o, --output PATH            Output file name  [required]
  -n, --number-of-url INTEGER  Number of URL.  [default: 1000]
  --minzoom INTEGER            Override Dataset MinZoom.
  --maxzoom INTEGER            Override Dataset MaxZoom.
  -q, --quiet                  Remove progressbar and other non-error output.
  --version                    Show the version and exit.
  --help                       Show this message and exit.
```

```
$ rio siege my_cog.tif -o test.txt
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
PATH=tiles/
EXT=.png
QUERYSTRING=?url=http://127.0.0.1:8000/world.tif
$(PROT)://$(HOST):$(PORT)/$(PATH)0/1/1$(EXT)$(QUERYSTRING)
$(PROT)://$(HOST):$(PORT)/$(PATH)0/0/2$(EXT)$(QUERYSTRING)
$(PROT)://$(HOST):$(PORT)/$(PATH)0/1/2$(EXT)$(QUERYSTRING)
$(PROT)://$(HOST):$(PORT)/$(PATH)0/1/1$(EXT)$(QUERYSTRING)
$(PROT)://$(HOST):$(PORT)/$(PATH)0/1/2$(EXT)$(QUERYSTRING)
```

## Contribution & Development

See [CONTRIBUTING.md](https://github.com/developmentseed/rio-siege/blob/main/CONTRIBUTING.md)

## Authors

Created by [Development Seed](<http://developmentseed.org>)

See [contributors](https://github.com/developmentseed/rio-siege/graphs/contributors) for a listing of individual contributors.

## License

See [LICENSE](https://github.com/developmentseed/rio-siege/blob/main/LICENSE)
