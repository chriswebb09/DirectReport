#!/usr/bin/env python3

import click
import sys
from pathlib import Path
import webbrowser

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
def item():
    pass


@cli.group()
def web_browser():
    pass


@click.command()
@click.option('--week', 'transformation', flag_value='week', default=True)
@click.option('--day', 'transformation', flag_value='day')
@click.option('--all', 'transformation', flag_value='all')
def list(transformation):
    if transformation == "weekly":
        week = ListBuilder.list_this_week()
        if week is not None:
            for week_item in week:
                print(str(week_item) + "\n")
    elif transformation == "daily":
        today = ListBuilder.list_today()
        if today is not None:
            for today_item in today:
                print(str(today_item) + "\n")
    elif transformation == "all":
        all = ListBuilder.list_all()
        if all is not None:
            for all_item in all:
                print(str(all_item) + "\n")


@click.command()
@click.option('--entry', help="Add new entry to list", prompt='What have you been working on? ')
def new(entry):
    topic = ""
    if click.confirm('Do you wan to add in topic?'):
        topic = click.prompt('Enter topic', type=str)
    builder.new(entry, topic)


@click.command()
@click.option('--id', help="Delete item with id", prompt='What is the id of the entry you wish to delete?')
def delete(id):
    ListBuilder.delete(id)


@click.command()
@click.option("--url", default="http://127.0.0.1:5000", help="URL to open in the web browser")
def launch(url):
    click.launch(url)
    app.run()


@click.command()
def mail():
    recipient="mail@test.com"
    subject="work for week"
    week = ListBuilder.list_this_week()
    body = ""
    if week is not None:
        for week_item in week:
            body += str(week_item["topic"]) + "\n"  + str(week_item["message"]) + "\n" + "\n"
    webbrowser.open('mailto:?to=' + recipient + '&subject=' + subject + '&body=' + body, new=1)


list_items.add_command(list)
item.add_command(new)
item.add_command(delete)
web_browser.add_command(launch)
web_browser.add_command(mail)

cli = click.CommandCollection(sources=[list_items, item, web_browser])

if __name__ == '__main__':
    cli()
