#!/usr/bin/env python3

from DirectReport.models.entry import Entry
from DirectReport.database.entry_storage import EntryStorage
from datetime import datetime
from pathlib import Path
import tempfile
import pytest
import uuid
import sys
import os

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
    storage = EntryStorage(temp_db)
    assert storage is not None
    # The table should be created without raising any exceptions


def test_add_get_entry(temp_db):
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
    retrieved_entry = storage.get_entry(entry.uuid)

    assert entry.message == retrieved_entry.message


def test_update_entry(temp_db):
    storage = EntryStorage(temp_db)
    entry = Entry(
        uuid=uuid.uuid4(),
        topic="Test Topic",
        message="Test message",
        created_at=datetime.now(),
        modified_on=datetime.now(),
        week_uuid=uuid.uuid4(),
    )
    storage.add_entry(entry)
    entry.message = "Updated message"
    entry.modified_on = datetime.now()
    storage.update_entry(entry)
    retrieved_entry = storage.get_entry(entry.uuid)
    assert entry.message == retrieved_entry.message


def test_delete_entry(temp_db):
    storage = EntryStorage(temp_db)
    entry = Entry(
        uuid=uuid.uuid4(),
        topic="New Topic",
        message="Test message",
        created_at=datetime.now(),
        modified_on=datetime.now(),
        week_uuid=uuid.uuid4(),
    )

    storage.add_entry(entry)
    storage.delete_entry(entry.uuid)
    retrieved_entry = storage.get_entry(entry.uuid)

    assert retrieved_entry is None


def test_get_all_entries(temp_db):
    storage = EntryStorage(temp_db)
    entry1 = Entry(
        uuid=uuid.uuid4(),
        topic="New",
        message="Test message 1",
        created_at=datetime.now(),
        modified_on=datetime.now(),
        week_uuid=uuid.uuid4(),
    )
    entry2 = Entry(
        uuid=uuid.uuid4(),
        topic="Topic new",
        message="Test message 2",
        created_at=datetime.now(),
        modified_on=datetime.now(),
        week_uuid=uuid.uuid4(),
    )

    storage.add_entry(entry1)
    storage.add_entry(entry2)

    entries = storage.list_all_entries()
    assert len(entries) == 2
    # assert entry1 in entries
    # assert entry2 in entries


def test_get_entries_by_week(temp_db):
    storage = EntryStorage(temp_db)
    week_uuid = uuid.uuid4()
    entry1 = Entry(
        uuid=uuid.uuid4(),
        topic="Topic",
        message="Test message 1",
        created_at=datetime.now(),
        modified_on=datetime.now(),
        week_uuid=week_uuid,
    )
    entry2: Entry = Entry(
        uuid=uuid.uuid4(),
        topic="Topic 3",
        message="Test message 2",
        created_at=datetime.now(),
        modified_on=datetime.now(),
        week_uuid=uuid.uuid4(),
    )

    storage.add_entry(entry1)
    storage.add_entry(entry2)

    entries = storage.get_entries_by_week(week_uuid)
    # et_entries_by_week(week_uuid)
    assert len(entries) == 1
