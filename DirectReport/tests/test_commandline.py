#!/usr/bin/env python3

from click.testing import CliRunner
from DirectReport.commandline.commandline import new
from DirectReport.commandline.commandline import list
from DirectReport.commandline.commandline import mail
from DirectReport.commandline.commandline import delete
from DirectReport.commandline.commandline import launch

runner = CliRunner()


def test_cli_prompt_new():
    response = runner.invoke(
        new,
        input='From the main menu, select Edit | Find | Find in Files Ctrl+Shift+F . In the search field, type your search string. Alternatively, in the editor, highlight the string you want to find and press Ctrl+Shift+F ',
    )
    assert response.exit_code is not None
    assert "What have you been working on" in response.output


def test_cli_list():
    response = runner.invoke(list)
    assert response.exit_code == 0


def test_cli_list_daily():
    result = runner.invoke(list, ['--day'])
    assert result.exit_code == 0


def test_cli_list_weekly():
    result = runner.invoke(list, ['--week'])
    assert result.exit_code == 0


def test_cli_list_all():
    result = runner.invoke(list, ['--all'])
    assert result.exit_code == 0

def test_cli_mail():
    result = runner.invoke(mail)
    assert result.exit_code == 0

def test_cli_delete():
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
    result = runner.invoke(delete, input=entry.uuid)
    assert result.exit_code == 0