#!/usr/bin/env python3

# from DirectReport.commandline.commandline import list
# from DirectReport.commandline.commandline import mail
# from click.testing import CliRunner
# import tempfile
# import pytest
# import os
# import sys
# from pathlib import Path
#
# file = Path(__file__).resolve()
# package_root_directory = file.parents[1]
# sys.path.append(str(package_root_directory))
#
# sys.path.append('.')
#
# runner = CliRunner()

# @pytest.fixture
# def temp_db():
#     db_fd, db_path = tempfile.mkstemp()
#     yield db_path
#     os.close(db_fd)
#     os.remove(db_path)
#

# def test_cli_prompt_new():
#     pass
#
#
# def test_cli_list():
#     response = runner.invoke(list)
#     assert response.exit_code == 0
#
#
# def test_cli_list_daily():
#     result = runner.invoke(list, ['--day'])
#     assert result.exit_code == 0
#
#
# def test_cli_list_all():
#     result = runner.invoke(list, ['--all'])
#     assert result.exit_code == 0
#
#
# def test_cli_mail():
#     result = runner.invoke(mail)
#     assert result.exit_code == 0
