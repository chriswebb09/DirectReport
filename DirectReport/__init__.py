#!/usr/bin/env python3

import sys

from pathlib import Path

file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))

if __name__ == '__main__':
    from browserview import app
    from commandline import commandline
    from models import entry
    from database import entry_storage, weekly_storage
else:
    from DirectReport.browserview import app
    from DirectReport.commandline import commandline
    from DirectReport.models import entry
    from DirectReport.database import entry_storage, weekly_storage


__version__ = "0.1.0"
