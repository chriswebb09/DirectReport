#!/usr/bin/env python3

import click
import sys
from pathlib import Path
import webbrowser

file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))

from DirectReport.browserview.app import app
from DirectReport.models.list_builder import ListBuilder

builder = ListBuilder()


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
@click.option('--week', 'transformation', flag_value='week', default=True)
@click.option('--day', 'transformation', flag_value='day')
@click.option('--notes', 'transformation', flag_value='notes')
@click.option('--all', 'transformation', flag_value='all')
def list(transformation):
    """
    Lists items based on the selected transformation flag.

    :param transformation: The selected transformation flag (week, day, or all).
    """

    if transformation == "week":
        week_id = ListBuilder.get_weekly_id()
        week = ListBuilder.list_week(week_id)
        if week == []:
            ListBuilder.add_new_weekly()
        if week is not None:
            for week_item in week:
                print(str(week_item) + "\n")
    elif transformation == "day":
        today = ListBuilder.list_today()
        if today is not None:
            print("today - " + str(today) + "\n")

    elif transformation == "all":
        all = ListBuilder.list_all()
        if all is not None:
            for all_item in all:
                print(str(all_item) + "\n")
    elif transformation == "notes":
        daily_id = ListBuilder.get_daily_id()
        all = ListBuilder.get_notes(daily_id)
        if all is not None:
            for all_item in all:
                print(str(all_item) + "\n")


@click.command()
@click.option('--entry', 'transformation', flag_value='entry', default=True, help="Add new entry to list")
@click.option('--note', 'transformation', flag_value='note', help="Add new entry to list")
@click.option('--blocker', 'transformation', flag_value='blocker', help="Add new blocker to list")
@click.option('--jira', 'transformation', flag_value='jira', help="Add new jira to list")
def new(transformation):
    """
    Adds a new entry to the list.

    :param entry: The entry text to add.
    """

    if transformation == "entry":
        if ListBuilder.week_exists() is False:
            ListBuilder.add_new_weekly()
        ListBuilder.add_new_daily()
        topic = click.prompt('Topic', type=str)
        entry = click.prompt('Goal', type=str)
        builder.new(entry, topic)
    if transformation == "note":
        if ListBuilder.week_exists() is False:
            ListBuilder.add_new_weekly()
            ListBuilder.add_new_daily()
        daily_id = ListBuilder.get_daily_id()
        note = ""
        note = click.prompt('Note', type=str)
        ListBuilder.add_new_note(note, daily_id)
    if transformation == "blocker":
        if ListBuilder.week_exists() is False:
            ListBuilder.add_new_weekly()
            ListBuilder.add_new_daily()
        daily_id = ListBuilder.get_daily_id()
        blocker = click.prompt('Blocker', type=str)
        ListBuilder.add_new_blocker(blocker, daily_id)
    if transformation == "jira":
        if ListBuilder.week_exists() is False:
            ListBuilder.add_new_weekly()
            ListBuilder.add_new_daily()
        daily_id = ListBuilder.get_daily_id()
        jira_ticket = click.prompt('Jira', type=str)
        jira_tag = click.prompt('Jira', type=str)
        ListBuilder.add_new_jira(jira_ticket, jira_tag, daily_id)


@click.command()
@click.option('--id', help="Delete item with id", prompt='What is the id of the entry you wish to delete?')
def delete(id):
    """
    Deletes an item with the specified ID.

    :param id: The ID of the item to delete.
    """
    ListBuilder.delete(id)


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
    week_id = ListBuilder.get_weekly_id()
    week = ListBuilder.list_week(week_id)
    body = ""
    if week is not None:
        for week_item in week:
            body += str(week_item["topic"]) + "\n" + str(week_item["message"]) + "\n" + "\n"
    webbrowser.open('mailto:?to=' + recipient + '&subject=' + subject + '&body=' + body, new=1)


list_items.add_command(list)
item.add_command(new)
item.add_command(delete)
web_browser.add_command(launch)
web_browser.add_command(mail)

cli = click.CommandCollection(sources=[list_items, item, web_browser])

if __name__ == '__main__':
    cli()
