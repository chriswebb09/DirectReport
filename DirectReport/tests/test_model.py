#!/usr/bin/env python3

import datetime
import uuid

from DirectReport.models.entry import Entry


def test_data_model_set_message():
    entry1 = Entry(
        uuid.uuid4(), "Topic", "test", datetime.datetime.now(), datetime.datetime.now(), uuid.uuid4(), uuid.uuid4()
    )
    assert entry1.message == "test"


def test_data_model_update_message():
    entry2 = Entry(
        uuid.uuid4(), "Topic", "test", datetime.datetime.now(), datetime.datetime.now(), uuid.uuid4(), uuid.uuid4()
    )
    entry2.set_message("test2")
    assert entry2.message == "test2"


def test_data_model_is_recent():
    entry3 = Entry(
        uuid.uuid4(), "Topic", "test", datetime.datetime.now(), datetime.datetime.now(), uuid.uuid4(), uuid.uuid4()
    )
    entry3.set_message("test2")
    assert True == entry3.is_recent()
