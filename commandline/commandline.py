#!/usr/bin/env python3

import uuid
import datetime
import click
from commandline.entry import DailyEntry
from .entry_storage import DailyEntryStorage

# @click.command()
# @click.option('--new', help='New entry')
# @click.option('--list', help='Previous entries')

def interface(entry):
    """Takes in ENTRY for DirectReport"""
    # print(entry)
    storage = DailyEntryStorage('SQLite_Python.db')
    storage.add_entry(entry[0])
    entries = storage.get_all_entries()
    for entry_item in entries:
        print(entry_item)
    # click.echo(entry)
    # app()


if __name__ == '__main__':
    print(__package__)
    print("Main")
    entry1 = DailyEntry(uuid.uuid4(), "test 2", datetime.datetime.now(), datetime.datetime.now(), uuid.uuid4())
    interface(entry1)