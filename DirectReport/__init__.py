#!/usr/bin/env python3
from DirectReport.browserview import app
from DirectReport.commandline import commandline, entry, entry_storage, storage, weekly_storage

file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))

__version__ = "0.1.0"
