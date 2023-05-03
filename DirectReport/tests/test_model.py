#!/usr/bin/env python3

from DirectReport.models.entry import Entry
import datetime
import uuid


def test_data_model_set_message():
    entry1 = Entry(uuid.uuid4(), "Topic", "test", datetime.datetime.now(), datetime.datetime.now(), uuid.uuid4())
    assert entry1.message == "test"


def test_data_model_update_message():
    entry2 = Entry(uuid.uuid4(), "Topic", "test", datetime.datetime.now(), datetime.datetime.now(), uuid.uuid4())
    entry2.set_message("test2")
    assert entry2.message == "test2"


def test_data_model_is_recent():
    entry3 = Entry(uuid.uuid4(), "Topic", "test", datetime.datetime.now(), datetime.datetime.now(), uuid.uuid4())
    entry3.set_message("test2")
    assert entry3.is_recent() is True
