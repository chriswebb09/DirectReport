#!/usr/bin/env python3

from click.testing import CliRunner
from DirectReport.commandline.commandline import new
from DirectReport.commandline.commandline import launch

runner = CliRunner()


def test_prompt_new():
    response = runner.invoke(new, input='wau wau\n')
    assert response.exit_code == 0
    assert "What have you been working on" in response.output


def test_prompt_launch():
    response = runner.invoke(launch)
    assert response.exit_code == 0
    assert "Serving Flask app 'DirectReport.browserview.app'" in response.output
