#!/usr/bin/env python3

import click
import sys
from browserview.app import app

from pathlib import Path
file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))

if __name__ == '__main__':
    from list_builder import ListBuilder
else:
    from .list_builder import ListBuilder

builder = ListBuilder()

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
    week = builder.list_this_week()
    if week is not None:
        for week_item in week:
            print(week_item)
            print(" ")
    else:
        print("week is none")


@click.command()
@click.option('--entry', prompt='What have you been working on')
def new(entry):
    builder.new(entry)
    week = builder.list_this_week()
    if week is not None:
        for week_item in week:
            print(week_item)
            print(" ")
    else:
        print("week is none")

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
