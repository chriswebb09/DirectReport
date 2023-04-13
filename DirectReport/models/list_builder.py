#!/usr/bin/env python3

import datetime
import sys
import uuid
from pathlib import Path

file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))

from DirectReport.database.daily_storage import DailyUUIDTable
from DirectReport.database.weekly_storage import WeekUUIDTable
from DirectReport.database.entry_storage import EntryStorage
from DirectReport.models.entry import Entry


class ListBuilder:
    """
    A class to facilitate creating, deleting and listing entries in a weekly and daily report system.
    """

    def __init__(self):
        pass

    @staticmethod
    def get_weekly_id():
        """
        Retrieves the weekly ID for the current week.

        :return: The weekly ID.
        """
        today = datetime.date.today()
        weekly = WeekUUIDTable('SQLite_Python.db')
        weekly.create_table()
        result = weekly.find_uuid_by_date(today)
        if result is None:
            return ListBuilder.add_new_weekly()
        else:
            return result

    @staticmethod
    def get_daily_id():
        """
        Retrieves the daily ID for the current day.

        :return: The daily ID.
        """
        today = datetime.date.today()
        daily = DailyUUIDTable('SQLite_Python.db')
        daily.create_table()
        result = daily.find_uuid_by_date(today)
        if result is None:
            return ListBuilder.add_new_daily()
        else:
            return result

    @staticmethod
    def add_new_weekly():
        """
        Adds a new weekly ID.

        :return: The newly created weekly ID.
        """
        today = datetime.date.today().strftime("%m/%d/%Y, %H:%M:%S")
        weekly = WeekUUIDTable('SQLite_Python.db')
        weekly_id = str(uuid.uuid4())
        weekly.add_uuid(today, weekly_id)
        return id

    @staticmethod
    def add_new_daily():
        """
        Adds a new daily ID.

        :return: The newly created daily ID.
        """
        today = datetime.date.today().strftime("%m/%d/%Y, %H:%M:%S")
        daily = DailyUUIDTable('SQLite_Python.db')
        daily.create_table()
        weekly_id = str(ListBuilder.get_weekly_id())
        daily_id = str(uuid.uuid4())
        daily.add_uuid(str(today), weekly_id, daily_id)
        return daily_id

    @staticmethod
    def new(entry, topic=None):
        """
        Creates a new entry with the given entry text and topic.

        :param entry: The entry text.
        :param topic: The topic for the entry (optional).
        """
        storage = EntryStorage('SQLite_Python.db')
        weekly_id = str(ListBuilder.get_weekly_id())
        daily_id = str(ListBuilder.get_daily_id())
        if topic is None or topic == '':
            topic = "Entry for work on " + str(datetime.datetime.now().strftime("%b %d, %Y"))

        new_entry = Entry(
            uuid.uuid4(),
            topic,
            entry,
            datetime.datetime.now(),
            datetime.datetime.now(),
            weekly_id,
            daily_id,
        )
        storage.add_entry(new_entry)

    @staticmethod
    def delete(entry_id):
        """
        Deletes an entry with the specified ID.

        :param entry_id: The ID of the entry to delete.
        """
        storage = EntryStorage('SQLite_Python.db')
        storage.delete_entry(entry_id)

    @staticmethod
    def list_all_daily_ids():
        """
        Lists all daily IDs.

        :return: A list of all daily IDs.
        """
        storage = DailyUUIDTable('SQLite_Python.db')
        list_all = storage.list_all_entries()
        return list_all

    @staticmethod
    def list_all_week_ids():
        """
        Lists all weekly IDs.

        :return: A list of all weekly IDs.
        """
        storage = WeekUUIDTable('SQLite_Python.db')
        list_all = storage.list_all_entries()
        return list_all

    @staticmethod
    def list_today():
        """
        Lists all entries for today.

        :return: A list of entries for today.
        """
        storage = EntryStorage('SQLite_Python.db')
        daily_id = str(ListBuilder.get_daily_id())
        daily_list = storage.get_entries_by_day(daily_id)
        return daily_list

    @staticmethod
    def list_week(weekly_id):
        """
        Lists all entries for a given week.

        :param weekly_id: The weekly ID to list entries for.
        :return: A list of entries for the specified week.
        """
        storage = EntryStorage('SQLite_Python.db')
        weekly_id = str(weekly_id)
        week_list = storage.get_entries_by_week(weekly_id)
        return week_list

    @staticmethod
    def list_this_week_as_json():
        """
        Lists all entries for the current week as JSON.

        :return: A JSON representation of all entries for the current week.
        """
        storage = EntryStorage('SQLite_Python.db')
        weekly_id = str(ListBuilder.get_weekly_id())
        week_list = []
        for item in storage.get_entries_by_week(weekly_id):
            week_list.append(item.to_dict())
        return week_list

    @staticmethod
    def list_all():
        """
        Lists all entries.

        :return: A list of all entries.
        """
        storage = EntryStorage('SQLite_Python.db')
        list_items = storage.get_all_entries()
        return list_items
