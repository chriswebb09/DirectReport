#!/usr/bin/env python3

import datetime
import uuid
from DirectReport.models.entry.entry import Entry
from DirectReport.models.entry.entry_storage import EntryStorage


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
        storage = EntryStorage('EntryStorage.db')
        storage.create_table()
        if topic_text is None or topic_text == '':
            topic_text = "Entry for work on " + str(today)
        new_entry = Entry(str(uuid.uuid1()), topic_text, entry_text, today, datetime.datetime.now().timestamp())
        storage.add_entry(new_entry)

    @staticmethod
    def update(uid, entry_text, topic_text, created_at):
        """
        Updates an entry with the given entry text and topic.
        :param uid: The entry id.
        :param entry_text: The entry text.
        :param topic_text: The topic for the entry
        :param created_at: The date entry was created.
        :param weekly_id: The weekly id.
        """
        storage = EntryStorage('EntryStorage.db')
        storage.create_table()
        new_entry = Entry(str(uuid.UUID(uid)), topic_text, entry_text, created_at, datetime.datetime.now().timestamp())
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
        storage = EntryStorage('EntryStorage.db')
        # daily_id = str(DailyBuilder.get_daily_id())
        # daily_list = storage.get_entry(daily_id)
        list = storage.list_all_entries()
        return list

    @staticmethod
    def list_all():
        """
        Lists all entries.
        :return: A list of all entries.
        """
        storage = EntryStorage('EntryStorage.db')
        list_items = storage.list_all_entries_as_dict()

        return list_items
