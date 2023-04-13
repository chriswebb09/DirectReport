#!/usr/bin/env python3

from DirectReport.database.weekly_storage import WeekUUIDTable
from DirectReport.models import list_builder
from datetime import datetime
from pathlib import Path
import tempfile
import pytest
import uuid
import os
import sys

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


def test_create_table(temp_db):
    weekly_storage = WeekUUIDTable(temp_db)
    weekly_storage.create_table()
    weekly_storage.add_uuid(str(datetime.now()), str(uuid.uuid4()))
    assert len(weekly_storage.list_all_entries()) == 1
