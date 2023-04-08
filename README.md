# DirectReport

![License](https://img.shields.io/github/license/chriswebb09/DirectReport)
![Issues](https://img.shields.io/github/issues/chriswebb09/DirectReport)
[![codecov](https://codecov.io/gh/chriswebb09/DirectReport/branch/main/graph/badge.svg?token=E802G1JVJ5)](https://codecov.io/gh/chriswebb09/DirectReport)

# Overview

Keep track of your accomplishments each day of the workweek, create a report of things you accomplished at the end of the week that you can email to manager.  Review progress each quarterly for more effective performance review.

## Installing

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
 ~/DirectReport: python DirectReport launch
 * Serving Flask app 'DirectReport.browserview.app'
 * Debug mode: off
 
```

### Show-List


#### Basic

```

 ~/DirectReport: python DirectReport show-list
 
{'uuid': 'dd3ac9aa-4bbf-4ad6-9b31-16df6a0a0e52', 'topic': 'Test Topic', 'message': 'test', 'created_at': '2023-04-08 09:41:43.821522', 'modified_on': '2023-04-08 09:41:43.821527', 'week_uuid': 'b4fc7c44-aade-4497-adf2-f988bbaa8950', 'day_uuid': '55a307f4-a62a-4148-a664-8dd1afcbd620'}

{'uuid': 'bfb5f5d7-a4db-4563-8c0e-e857adb1ce7b', 'topic': 'Test Topic', 'message': 'I have been working on work', 'created_at': '2023-04-08 09:41:54.566438', 'modified_on': '2023-04-08 09:41:54.566451', 'week_uuid': 'b4fc7c44-aade-4497-adf2-f988bbaa8950', 'day_uuid': '09f7986d-5056-478f-b4ba-5e07929bb5cb'}

```


#### All

```

 ~/DirectReport: python DirectReport show-list --all
{  uuid : 4ec312e8-8ebe-4a74-825d-4d0c811bd0bd  topic :   message : I am working on the railroad  created_at : 2023-04-08 10:53:34.054188  modified_on : 2023-04-08 10:53:34.054193  week_uuid : 319df1b2-8681-4d33-abdb-3051c7fd6ca5  day_uuid : c6e86041-fe13-43e5-9c2c-5a3aecf77c77  }
 
 ```
 
 #### Daily
 
 ```
 
 ~/DirectReport: python DirectReport show-list --daily
{  uuid : 4ec312e8-8ebe-4a74-825d-4d0c811bd0bd  topic :   message : I am working on the railroad  created_at : 2023-04-08 10:53:34.054188  modified_on : 2023-04-08 10:53:34.054193  week_uuid : 319df1b2-8681-4d33-abdb-3051c7fd6ca5  day_uuid : c6e86041-fe13-43e5-9c2c-5a3aecf77c77  }

```

 #### Weekly

```

 ~/DirectReport: python DirectReport show-list --weekly
{  uuid : 4ec312e8-8ebe-4a74-825d-4d0c811bd0bd  topic :   message : I am working on the railroad  created_at : 2023-04-08 10:53:34.054188  modified_on : 2023-04-08 10:53:34.054193  week_uuid : 319df1b2-8681-4d33-abdb-3051c7fd6ca5  day_uuid : c6e86041-fe13-43e5-9c2c-5a3aecf77c77  }

```
