#!/usr/bin/env python3

from DirectReport.commandline.commandline import list
from DirectReport.commandline.commandline import mail
from DirectReport.commandline.commandline import delete
from DirectReport.database.entry_storage import EntryStorage
from DirectReport.models.entry import Entry
from click.testing import CliRunner
from datetime import datetime
import tempfile
import pytest
import os
import uuid


runner = CliRunner()


@pytest.fixture
def temp_db():
    db_fd, db_path = tempfile.mkstemp()
    yield db_path
    os.close(db_fd)
    os.remove(db_path)


def test_cli_prompt_new():
    pass
    # response = runner.invoke(new, input='From the main menu, select Edit | Find | Find in Files Ctrl+Shift+F . In the search field, type your search string. Alternatively, in the editor, highlight the string you want to find and press Ctrl+Shift+F')
    # assert response.exit_code is not None
    # assert "What have you been working on" in response.output


def test_cli_list():
    response = runner.invoke(list)
    assert response.exit_code == 0


def test_cli_list_daily():
    result = runner.invoke(list, ['--day'])
    assert result.exit_code == 1


def test_cli_list_weekly():
    result = runner.invoke(list, ['--week'])
    assert result.exit_code == 0


def test_cli_list_all():
    result = runner.invoke(list, ['--all'])
    assert result.exit_code == 0


def test_cli_mail():
    result = runner.invoke(mail)
    assert result.exit_code == 0


def test_cli_delete(temp_db):
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
    result = runner.invoke(delete, input=str(entry.uuid).encode())
    assert result.exit_code == 1
