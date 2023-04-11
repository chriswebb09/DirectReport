#!/usr/bin/env python3

import click
import sys
from pathlib import Path

file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))

if __name__ == '__main__':
    from browserview.app import app
    from models.list_builder import ListBuilder
else:
    from DirectReport.browserview.app import app
    from DirectReport.models.list_builder import ListBuilder


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
def web_browser():
    pass


@click.command()
@click.option('--weekly', 'transformation', flag_value='weekly', default=True)
@click.option('--daily', 'transformation', flag_value='daily')
@click.option('--all', 'transformation', flag_value='all')
def show_list(transformation):
    if transformation == "weekly":
        week = ListBuilder.list_this_week()
        if week is not None:
            for week_item in week:
                print(str(week_item) + "\n")
        else:
            print("week is none")
    elif transformation == "daily":
        today = ListBuilder.list_today()
        if today is not None:
            for today_item in today:
                print(str(today_item) + "\n")
        else:
            print("Today is none")
    elif transformation == "all":
        all = ListBuilder.list_all()
        if all is not None:
            for all_item in all:
                print(str(all_item) + "\n")
        else:
            print("All is none")


@click.command()
@click.option('--entry', help="Add new entry to list", prompt='What have you been working on')
def new(entry):
    topic = ""
    if click.confirm('Do you wan to add in topic?'):
        topic = click.prompt('Enter topic', type=str)
    builder.new(entry, topic)


@click.command()
@click.option("--url", default="http://127.0.0.1:5000", help="URL to open in the web browser")
def launch(url):
    click.launch(url)
    app.run()


list_items.add_command(show_list)
new_item.add_command(new)
web_browser.add_command(launch)

cli = click.CommandCollection(sources=[list_items, new_item, web_browser])

if __name__ == '__main__':
    cli()
