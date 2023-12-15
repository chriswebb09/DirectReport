#!/usr/bin/env python3

import os
import sys
import tempfile
from pathlib import Path

import pytest

file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))

sys.path.append('.')


@pytest.fixture
def temp_db():
    db_fd, db_path = tempfile.mkstemp()
    yield db_path
    os.close(db_fd)
    os.remove(db_path)
