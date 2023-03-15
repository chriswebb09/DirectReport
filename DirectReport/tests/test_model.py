#!/usr/bin/env python3

import pytest
from commandline.entry import DailyEntry
import uuid
import datetime

def test_data_model_set_message():
    entry1 = DailyEntry(uuid.uuid4(), "test", datetime.datetime.now(), datetime.datetime.now(), uuid.uuid4())
    assert entry1.message == "test"

def test_data_model_update_message():
    entry2 = DailyEntry(uuid.uuid4(), "test", datetime.datetime.now(), datetime.datetime.now(), uuid.uuid4())
    entry2.set_message("test2")
    assert entry2.message == "test2"

def test_data_model_is_recent():
    entry3 = DailyEntry(uuid.uuid4(), "test", datetime.datetime.now(), datetime.datetime.now(), uuid.uuid4())
    entry3.set_message("test2")
    assert entry3.is_recent() == True