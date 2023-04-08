#!/usr/bin/env python3

import datetime
import sys
import uuid
from pathlib import Path

file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))

if __name__ == '__main__':
    from ..database.weekly_storage import WeekUUIDTable
    from ..models.entry import DailyEntry
    from ..database.entry_storage import DailyEntryStorage
else:
    from database.weekly_storage import WeekUUIDTable
    from database.entry_storage import DailyEntryStorage
    from models.entry import DailyEntry


class ListBuilder:
    def __init__(self):
        pass

    @staticmethod
    def get_weekly_id():
        today = datetime.date.today()
        weekly = WeekUUIDTable('SQLite_Python.db')
        weekly.create_table()
        result = weekly.find_uuid_by_date(today)
        if result is None:
            return ListBuilder.add_new_weekly()
        else:
            return result

    @staticmethod
    def add_new_weekly():
        today = datetime.date.today()
        weekly = WeekUUIDTable('SQLite_Python.db')
        id = str(uuid.uuid4())
        weekly.add_uuid(today, id)
        return id

    def new(self, entry):
        storage = DailyEntryStorage('SQLite_Python.db')
        weekly_id = str(self.get_weekly_id())
        new_entry = DailyEntry(
            uuid.uuid4(), "Test Topic", entry, datetime.datetime.now(), datetime.datetime.now(), weekly_id, uuid.uuid4()
        )
        storage.add_entry(new_entry)

    def list_all_week_ids(self):
        storage = DailyEntryStorage('SQLite_Python.db')
        list_all = storage.get_all_entries()
        return list_all

    def list_this_week(self):
        storage = DailyEntryStorage('SQLite_Python.db')
        weekly_id = str(self.get_weekly_id())
        week_list = storage.get_entries_by_week(weekly_id)
        return week_list

    def list_this_week_as_json(self):
        storage = DailyEntryStorage('SQLite_Python.db')
        weekly_id = str(self.get_weekly_id())
        week_list = []
        for item in storage.get_entries_by_week(weekly_id):
            week_list.append(item.to_dict())
        return week_list


if __name__ == '__main__':
    print("main")