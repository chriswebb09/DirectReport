#!/usr/bin/env python3

from DirectReport.models.entry import Entry
from DirectReport.database.entry_storage import EntryStorage
from DirectReport.models import list_builder
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
    builder = list_builder.ListBuilder()
    storage = EntryStorage(temp_db)
    entry = Entry(
        uuid=uuid.uuid4(),
        topic="My topic",
        message="Test message",
        created_at=datetime.now(),
        modified_on=datetime.now(),
        week_uuid=uuid.uuid4(),
        day_uuid=uuid.uuid4(),
    )

    storage.add_entry(entry)
    assert len(builder.get_weekly_id()) is not None


def get_all_weekly_ids(temp_db):
    builder = list_builder.ListBuilder()
    storage = EntryStorage(temp_db)
    entry = Entry(
        uuid=uuid.uuid4(),
        topic="My topic",
        message="Test message",
        created_at=datetime.now(),
        modified_on=datetime.now(),
        week_uuid=uuid.uuid4(),
        day_uuid=uuid.uuid4(),
    )

    storage.add_entry(entry)
    assert len(list_builder.ListBuilder.list_all_daily_ids()) == 1


def get_all_daily_ids(temp_db):
    builder = list_builder.ListBuilder()
    storage = EntryStorage(temp_db)
    entry = Entry(
        uuid=uuid.uuid4(),
        topic="My topic",
        message="Test message",
        created_at=datetime.now(),
        modified_on=datetime.now(),
        week_uuid=uuid.uuid4(),
        day_uuid=uuid.uuid4(),
    )
    storage.add_entry(entry)
    assert len(list_builder.ListBuilder.list_all_daily_ids()) == 1
