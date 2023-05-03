#!/usr/bin/env python3

import datetime
import uuid

from DirectReport.models.entry import Entry
from DirectReport.database.entry_storage import EntryStorage
from DirectReport.models.weekly_builder import WeeklyBuilder
from DirectReport.models.daily_builder import DailyBuilder


class ListBuilder:

    """
    A class to facilitate creating, deleting and listing entries in a weekly and daily report system.
    """

    def __init__(self):
        pass

    @staticmethod
    def new(entry_text, topic_text=None):
        """
        Creates a new entry with the given entry text and topic.

        :param entry_text: The entry text.
        :param topic_text: The topic for the entry (optional).
        """
        today = datetime.date.today().strftime("%m/%d/%Y")
        storage = EntryStorage('SQLite_Python.db')
        print(storage.get_uuid(today))
        if storage.get_uuid(today) is not None:
            return
        DailyBuilder.add_new_daily()
        WeeklyBuilder.add_new_weekly()
        weekly_id = str(WeeklyBuilder.get_weekly_id())
        daily_id = str(DailyBuilder.get_daily_id())

        if topic_text is None or topic_text == '':
            topic_text = "Entry for work on " + str(datetime.datetime.now().strftime("%b %d, %Y"))
        new_entry = Entry(daily_id, topic_text, entry_text, datetime.datetime.now(), datetime.datetime.now(), weekly_id)
        storage.add_entry(new_entry)

    @staticmethod
    def update(uid, entry_text, topic_text, created_at, weekly_id):
        """
        Updates an entry with the given entry text and topic.

        :param uid: The entry id.
        :param entry_text: The entry text.
        :param topic_text: The topic for the entry
        :param created_at: The date entry was created.
        :param weekly_id: The weekly id.
        """
        storage = EntryStorage('SQLite_Python.db')
        storage.create_table()
        new_entry = Entry(str(uuid.UUID(uid)), topic_text, entry_text, created_at, datetime.datetime.now(), weekly_id)
        storage.update_entry(new_entry)

    @staticmethod
    def delete(entry_id):
        """
        Deletes an entry with the specified ID.

        :param entry_id: The ID of the entry to delete.
        """
        storage = EntryStorage('SQLite_Python.db')
        storage.delete_entry(entry_id)

    @staticmethod
    def list_today():
        """
        Lists all entries for today.

        :return: A list of entries for today.
        """

        storage = EntryStorage('SQLite_Python.db')
        daily_id = str(DailyBuilder.get_daily_id())
        daily_list = storage.get_entry(daily_id)
        return daily_list

    @staticmethod
    def list_all():
        """
        Lists all entries.

        :return: A list of all entries.
        """
        storage = EntryStorage('SQLite_Python.db')
        list_items = storage.list_all_entries()
        return list_items
