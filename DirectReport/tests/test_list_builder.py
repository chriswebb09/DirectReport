#!/usr/bin/env python3

from DirectReport.models.entry import Entry
from DirectReport.models.entry_storage import EntryStorage
import tempfile
import uuid
import os
from datetime import datetime
import pytest
import sys
from pathlib import Path

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

