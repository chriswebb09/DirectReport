#!/usr/bin/env python
from commandline import storage
from commandline import commandline
from browserview import app
from commandline import entry
import uuid
import datetime

def test():
    store = storage.DataStorage()
    store.makeDBConnection()
    entry1 = entry.DailyEntry(uuid.uuid4(), "test", datetime.datetime.now(), datetime.datetime.now(), uuid.uuid4())
    commandline.interface([entry1])


if __name__ == "__main__":
    commandline.cli()