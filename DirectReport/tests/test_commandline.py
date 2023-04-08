#!/usr/bin/env python3

from click.testing import CliRunner
from DirectReport.commandline.commandline import new
from DirectReport.commandline.commandline import show_list
from DirectReport.commandline.commandline import launch

runner = CliRunner()


def test_prompt_new():
    response = runner.invoke(new, input='wau wau\n')
    assert response.exit_code is not None
    assert "What have you been working on" in response.output


def test_cli_list():
    response = runner.invoke(show_list)
    assert response.exit_code == 0


#
# def test_prompt_launch():
#     response = runner.invoke(launch);
#     response = runner.invoke(runner.commands['launch'].commands['url'], input='http://127.0.0.1:5000/shutdown')
#     exit(0)
#     assert response.exit_code == 0
#     assert "Serving Flask app 'DirectReport.browserview.app'" in response.output
