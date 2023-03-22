#!/usr/bin/env python3

import os
import tempfile
import uuid
from datetime import datetime
import pytest
from DirectReport.commandline.entry_storage import DailyEntryStorage
from DirectReport.commandline.entry import DailyEntry


@pytest.fixture
def temp_db():
    db_fd, db_path = tempfile.mkstemp()
    yield db_path
    os.close(db_fd)
    os.remove(db_path)


def test_create_table(temp_db):
    storage = DailyEntryStorage(temp_db)
    # The table should be created without raising any exceptions


def test_add_get_entry(temp_db):
    storage = DailyEntryStorage(temp_db)
    entry = DailyEntry(
        uuid=uuid.uuid4(),
        message="Test message",
        created_at=datetime.now(),
        modified_on=datetime.now(),
        week_uuid=uuid.uuid4()
    )

    storage.add_entry(entry)
    retrieved_entry = storage.get_entry(entry.uuid)

    assert entry == retrieved_entry


def test_update_entry(temp_db):
    storage = DailyEntryStorage(temp_db)
    entry = DailyEntry(
        uuid=uuid.uuid4(),
        message="Test message",
        created_at=datetime.now(),
        modified_on=datetime.now(),
        week_uuid=uuid.uuid4()
    )

    storage.add_entry(entry)
    entry.message = "Updated message"
    entry.modified_on = datetime.now()

    storage.update_entry(entry)
    retrieved_entry = storage.get_entry(entry.uuid)

    assert entry == retrieved_entry


def test_delete_entry(temp_db):
    storage = DailyEntryStorage(temp_db)
    entry = DailyEntry(
        uuid=uuid.uuid4(),
        message="Test message",
        created_at=datetime.now(),
        modified_on=datetime.now(),
        week_uuid=uuid.uuid4()
    )

    storage.add_entry(entry)
    storage.delete_entry(entry.uuid)
    retrieved_entry = storage.get_entry(entry.uuid)

    assert retrieved_entry is None


def test_get_all_entries(temp_db):
    storage = DailyEntryStorage(temp_db)
    entry1 = DailyEntry(
        uuid=uuid.uuid4(),
        message="Test message 1",
        created_at=datetime.now(),
        modified_on=datetime.now(),
        week_uuid=uuid.uuid4()
    )
    entry2 = DailyEntry(
        uuid=uuid.uuid4(),
        message="Test message 2",
        created_at=datetime.now(),
        modified_on=datetime.now(),
        week_uuid=uuid.uuid4()
    )

    storage.add_entry(entry1)
    storage.add_entry(entry2)

    entries = storage.get_all_entries()
    assert len(entries) == 2
    assert entry1 in entries
    assert entry2 in entries


def test_get_entries_by_week(temp_db):
    storage = DailyEntryStorage(temp_db)
    week_uuid = uuid.uuid4()
    entry1 = DailyEntry(
        uuid=uuid.uuid4(),
        message="Test message 1",
        created_at=datetime.now(),
        modified_on=datetime.now(),
        week_uuid=week_uuid
    )
    entry2: DailyEntry = DailyEntry(
        uuid=uuid.uuid4(),
        message="Test message 2",
        created_at=datetime.now(),
        modified_on=datetime.now(),
        week_uuid=uuid.uuid4()
    )

    storage.add_entry(entry1)
    storage.add_entry(entry2)

    entries = storage.get_entries_by_week(week_uuid)
    assert len(entries) == 1
    assert entry1 in entries
