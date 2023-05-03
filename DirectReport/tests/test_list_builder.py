#!/usr/bin/env python3

from DirectReport.models.entry import Entry
from DirectReport.database.entry_storage import EntryStorage
from DirectReport.models.list_builder import ListBuilder
from DirectReport.models.weekly_builder import WeeklyBuilder
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


def test_get_weekly_id(temp_db):
    storage = EntryStorage(temp_db)
    entry = Entry(
        uuid=uuid.uuid4(),
        topic="My topic",
        message="Test message",
        created_at=datetime.now(),
        modified_on=datetime.now(),
        week_uuid=uuid.uuid4(),
    )

    storage.add_entry(entry)
    assert WeeklyBuilder.get_weekly_id() is not None
