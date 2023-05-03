#!/usr/bin/env python3

from DirectReport.database.daily_storage import DailyUUIDTable
from DirectReport.database.weekly_storage import WeekUUIDTable
from DirectReport.database.entry_storage import EntryStorage
from DirectReport.database.notes_storage import NotesDataStore
from DirectReport.models.entry import Entry
from pathlib import Path
import datetime
import sys
import uuid

file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))


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
    def week_exists():
        today = datetime.date.today().strftime("%m/%d/%Y")
        weekly = WeekUUIDTable('SQLite_Python.db')
        if weekly.get_uuid(today) is None:
            return False
        else:
            return True
    @staticmethod
    def add_new_weekly():
        """
        Adds a new weekly ID.

        :return: The newly created weekly ID.
        """
        today = datetime.date.today().strftime("%m/%d/%Y")
        weekly = WeekUUIDTable('SQLite_Python.db')
        weekly_id = ""
        if weekly.get_uuid(today) is None:
            weekly_id = str(uuid.uuid4())
            weekly.add_uuid(today, weekly_id)
        else:
            weekly_id = weekly.get_uuid(today)
        return weekly_id

    @staticmethod
    def add_new_daily():
        """
        Adds a new daily ID.

        :return: The newly created daily ID.
        """
        today = datetime.date.today().strftime("%m/%d/%Y")
        daily = DailyUUIDTable('SQLite_Python.db')
        daily.create_table()
        weekly_id = str(ListBuilder.get_weekly_id())
        daily_id = ""
        if daily.get_uuid(today) is not None:
            daily_id = daily.get_uuid(today)
        else:
            daily_id = str(uuid.uuid4())
            daily.add_uuid(str(today), weekly_id, daily_id)
        return daily_id

    @staticmethod
    def add_new_note(note_text, associated_id):
        """
        Adds a new daily ID.

        :return: The newly created daily ID.
        """

        notes = NotesDataStore('SQLite_Python.db')
        notes.add_notes_entry(note_text, associated_id)

    @staticmethod
    def get_notes(associated_id):
        """
        TODO
        """

        notes = NotesDataStore('SQLite_Python.db')
        note_list = notes.entries_for_associated_uuid(associated_id)
        print(note_list)
        return note_list

    @staticmethod
    def new(entry, topic=None):
        """
        Creates a new entry with the given entry text and topic.

        :param entry: The entry text.
        :param topic: The topic for the entry (optional).
        """
        today = datetime.date.today().strftime("%m/%d/%Y")
        storage = EntryStorage('SQLite_Python.db')
        print(storage.get_uuid(today))
        if storage.get_uuid(today) is not None:
            return
        ListBuilder.add_new_daily()
        ListBuilder.add_new_weekly()
        weekly_id = str(ListBuilder.get_weekly_id())
        daily_id = str(ListBuilder.get_daily_id())

        if topic is None or topic == '':
            topic = "Entry for work on " + str(datetime.datetime.now().strftime("%b %d, %Y"))
        new_entry = Entry(
            daily_id,
            topic,
            entry,
            datetime.datetime.now(),
            datetime.datetime.now(),
            weekly_id
        )
        storage.add_entry(new_entry)

    @staticmethod
    def update(id, entry, topic, created_at, weekly_id, daily_id):
        """
        Updates an entry with the given entry text and topic.

        :param id: The entry id.
        :param entry: The entry text.
        :param topic: The topic for the entry
        :param created_at: The date entry was created.
        :param weekly_id: The weekly id.
        :param daily_id: The daily id.
        """
        storage = EntryStorage('SQLite_Python.db')
        storage.create_table()
        new_entry = Entry(
            uuid.UUID(id),
            topic,
            entry,
            created_at,
            datetime.datetime.now(),
            weekly_id
        )
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
        daily_list = storage.get_entry(daily_id)
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
