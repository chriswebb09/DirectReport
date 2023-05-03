#!/usr/bin/env python3

import click
import sys
from pathlib import Path
import webbrowser
from DirectReport.browserview.app import app
from DirectReport.models.list_builder import ListBuilder
from DirectReport.models.weekly_builder import WeeklyBuilder
from DirectReport.models.daily_builder import DailyBuilder
from DirectReport.models.note.note_builder import NoteBuilder
from DirectReport.models.blocker_models.block_builder import BlockerBuilder
from DirectReport.models.jira_models.jira_builder import JiraBuilder

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
        week_id = WeeklyBuilder.get_weekly_id()
        week = WeeklyBuilder.list_week(week_id)
        if not week:
            WeeklyBuilder.add_new_weekly()
        if week is not None:
            for week_item in week:
                print(str(week_item) + "\n")
    elif transformation == "day":
        today = ListBuilder.list_today()
        if today is not None:
            print("today - " + str(today) + "\n")

    elif transformation == "all":
        all_list = ListBuilder.list_all()
        if all_list is not None:
            for all_item in all_list:
                print(str(all_item) + "\n")
    elif transformation == "notes":
        daily_id = DailyBuilder.get_daily_id()
        all_list = NoteBuilder.get_notes(daily_id)
        if all_list is not None:
            for all_item in all_list:
                print(str(all_item) + "\n")


@click.command()
@click.option('--entry', 'transformation', flag_value='entry', default=True, help="Add new entry to list")
@click.option('--note', 'transformation', flag_value='note', help="Add new entry to list")
@click.option('--blocker_models', 'transformation', flag_value='blocker_models', help="Add new blocker_models to list")
@click.option('--jira_models', 'transformation', flag_value='jira_models', help="Add new jira_models to list")
def new(transformation):
    """
    Adds a new entry to the list.

    :param transformation: The entry text to add.
    """
    if transformation == "entry":
        if WeeklyBuilder.week_exists() is False:
            WeeklyBuilder.add_new_weekly()
        DailyBuilder.add_new_daily()
        topic = click.prompt('Topic', type=str)
        entry = click.prompt('Goal', type=str)
        ListBuilder.new(entry, topic)
    else:
        if WeeklyBuilder.week_exists() is False:
            DailyBuilder.add_new_weekly()
            DailyBuilder.add_new_daily()
        if transformation == "note":
            daily_id = DailyBuilder.get_daily_id()
            note = click.prompt('Note', type=str)
            NoteBuilder.add_new_note(note, daily_id)
        if transformation == "blocker_models":
            if WeeklyBuilder.week_exists() is False:
                daily_id = DailyBuilder.get_daily_id()
            blocker = click.prompt('Blocker', type=str)
            BlockerBuilder.add_new_blocker(blocker, daily_id)
        if transformation == "jira_models":
            daily_id = DailyBuilder.get_daily_id()
            jira_ticket = click.prompt('Jira', type=str)
            jira_tag = click.prompt('Jira', type=str)
            JiraBuilder.add_new_jira(jira_ticket, jira_tag, daily_id)


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
    week_id = WeeklyBuilder.get_weekly_id()
    week = WeeklyBuilder.list_week(week_id)
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
