#!/usr/bin/env python3

import uuid
import datetime
import click
import sys
from browserview.app import app

from pathlib import Path
file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))

if __name__ == '__main__':
    from entry import DailyEntry
    from entry_storage import DailyEntryStorage
else:
    from .entry import DailyEntry
    from .entry_storage import DailyEntryStorage

@click.group()
def cli():
    pass

@cli.group()
def list_items():
    pass

@cli.group()
def new_item():
    pass

@cli.group()
def webbrowser():
    pass

@click.command()
def list():
    storage = DailyEntryStorage('SQLite_Python.db')
    entries = storage.get_all_entries()
    for entry_item in entries:
        print(entry_item)

@click.command()
def new():
    entry1 = DailyEntry(uuid.uuid4(), "test 2", datetime.datetime.now(), datetime.datetime.now(), uuid.uuid4())
    storage = DailyEntryStorage('SQLite_Python.db')
    entries = storage.add_entry(entry1)

@click.command()
def launch():
    click.launch('http://127.0.0.1:5000')
    app.run()

list_items.add_command(list)
new_item.add_command(new)
webbrowser.add_command(launch)

cli = click.CommandCollection(sources=[list_items, new_item, webbrowser])

if __name__ == '__main__':
    cli()
