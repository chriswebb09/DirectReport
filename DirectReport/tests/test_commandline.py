#!/usr/bin/env python3

from click.testing import CliRunner
from DirectReport.commandline.commandline import new
from DirectReport.commandline.commandline import list
from DirectReport.commandline.commandline import launch

runner = CliRunner()


def test_prompt_new():
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


#
# def test_prompt_launch():
#     response = runner.invoke(launch);
#     response = runner.invoke(runner.commands['launch'].commands['url'], input='http://127.0.0.1:5000/shutdown')
#     exit(0)
#     assert response.exit_code == 0
#     assert "Serving Flask app 'DirectReport.browserview.app'" in response.output
