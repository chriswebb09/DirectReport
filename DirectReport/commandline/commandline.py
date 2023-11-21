#!/usr/bin/env python3

import click
import sys
from pathlib import Path
import webbrowser
from DirectReport.browserview.app import app
from DirectReport.models.list_builder import ListBuilder

file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))
@click.group()
def cli():
    """Main Click group for the command line interface."""
    pass
@cli.group()
def list_items():
    """Click group for list items related commands."""
    pass
@cli.group()
def item():
    """Click group for item related commands."""
    pass
@cli.group()
def web_browser():
    """Click group for web browser related commands."""
    pass
@click.command()
@click.option('--day', 'transformation', flag_value='day')
@click.option('--all', 'transformation', flag_value='all')
def list(transformation):
    """
    Lists items based on the selected transformation flag.
    :param transformation: The selected transformation flag (week, day, or all).
    """
    if transformation == "day":
        today = ListBuilder.list_today()
        if today is not None:
            print("today - " + str(today) + "\n")
    elif transformation == "all":
        all_list = ListBuilder.list_all()
        if all_list is not None:
            for all_item in all_list:
                print(str(all_item) + "\n")
@click.command()
@click.option('--entry', 'transformation', flag_value='entry', default=True, help="Add new entry to list")
def new(transformation):
    """
    Adds a new entry to the list.
    :param transformation: The entry text to add.
    """
    if transformation == "entry":
        topic = click.prompt('Topic', type=str)
        entry = click.prompt('Goal', type=str)
        ListBuilder.new(entry, topic)
        return
@click.command()
@click.option('--id', help="Delete item with id", prompt='What is the id of the entry you wish to delete?')
def delete(uid):
    """
    Deletes an item with the specified ID.
    :param uid: The ID of the item to delete.
    """
    ListBuilder.delete(uid)
@click.command()
@click.option("--url", default="http://127.0.0.1:5000", help="URL to open in the web browser")
def launch(url):
    """
    Launches the web browser and runs the app.
    :param url: The URL to open in the web browser.
    """
    click.launch(url)
    app.run()
@click.command()
def mail():
    """
    Sends an email with the week's work items.
    """
    recipient = "mail@test.com"
    subject = "work for week"
    body = ""
    webbrowser.open('mailto:?to=' + recipient + '&subject=' + subject + '&body=' + body, new=1)

list_items.add_command(list)
item.add_command(new)
item.add_command(delete)
web_browser.add_command(launch)
web_browser.add_command(mail)

cli = click.CommandCollection(sources=[list_items, item, web_browser])

if __name__ == '__main__':
    cli()