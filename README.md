# DirectReport

![License](https://img.shields.io/github/license/chriswebb09/DirectReport)
![Issues](https://img.shields.io/github/issues/chriswebb09/DirectReport)
![codecov](https://codecov.io/gh/chriswebb09/DirectReport/branch/main/graph/badge.svg?token=E802G1JVJ5)
![build](https://github.com/chriswebb09/DirectReport/actions/workflows/build.yml/badge.svg)
![GitHub Latest Release](https://img.shields.io/github/v/release/chriswebb09/DirectReport?logo=github)
![ReadTheDocs](https://readthedocs.org/projects/directreport/badge/?version=latest)


# Overview

Keep track of your accomplishments each day of the workweek, create a report of things you accomplished at the end of the week that you can email to manager.  Review progress each quarterly for more effective performance review.

## Documentation 

[Github Page](https://chriswebb09.github.io/DirectReport/)

## Installing

### From Package Manager 

Using pip: 
`pip install DirectReport`

### From Project Files: 

This project uses a `Makefile` as a command registry, with the following commands:
- `make`: list available commands
- `make develop`: install and build this library and its dependencies using `pip`
- `make build`: build the library using `setuptools`
- `make lint`: perform static analysis of this library with `flake8` and `black`
- `make format`: autoformat this library using `black`
- `make annotate`: run type checking using `mypy`
- `make test`: run automated tests with `pytest`
- `make coverage`: run automated tests with `pytest` and collect coverage information
- `make dist`: package library for distribution

Adapted From: https://github.com/ColumbiaOSS/example-project-python

## Running Direct Report

### Overview

```

Usage: python -m DirectReport [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  launch
  new
  show-list
  
```

### Launch

```
$ python DirectReport launch
```

### Show-List


#### Basic

```
 $ python DirectReport list
```


#### All

```
$ python DirectReport list --all
 ```
 
#### Daily
 
 ```
$ python DirectReport list --day
```

#### Weekly

```

$ python DirectReport list --week

```

## Web Interface

### Home

Web interface home page - WIP

![Screenshot home page for web interface.](DirectReport/assets/web_interface.png)

### List

Web interface for list page - WIP

![Screenshot list page for web interface.](DirectReport/assets/web_interface2.png)

### Detail

![Screenshot detail page for web interface.](DirectReport/assets/web_interface4.png)
