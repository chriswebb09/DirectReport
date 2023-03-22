#!/usr/bin/env python3

import sys

from pathlib import Path

file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))

if __name__ == '__main__':
    from .browserview import app
    from .commandline import commandline, entry, entry_storage, storage, weekly_storage
else:
    from browserview import app
    from commandline import commandline, entry, entry_storage, storage, weekly_storage


__version__ = "0.1.0"
