#!/usr/bin/env python3

from DirectReport.models.entry import Entry
from DirectReport.database.entry_storage import EntryStorage
import os

import tempfile
import uuid
from datetime import datetime
from pathlib import Path
import sys
from DirectReport.browserview.app import app

file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))

sys.path.append('.')

import pytest

def test_index_route():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.data.decode('utf-8').__contains__('<meta charset="utf-8"/>')

def test_list_route():
    response = app.test_client().get('/list')
    assert response.status_code == 200
    assert response.data.decode('utf-8').__contains__('<meta charset="utf-8"/>')

def test_404_route():
    response = app.test_client().get('/wiki')
    assert response.status_code == 404
    assert response.data.decode('utf-8').__contains__('404')