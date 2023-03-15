#!/usr/bin/env python3

import uuid
import datetime
import sys

from pathlib import Path
file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))

if __name__ == '__main__':
    from weekly_storage import DateUUIDTable
    from entry_storage import DailyEntryStorage
    from entry import DailyEntry
else:
    from .weekly_storage import DateUUIDTable
    from .entry import DailyEntry
    from .entry_storage import DailyEntryStorage

class ListBuilder:

    def __init__(self):
        pass
        # self.weekly = DateUUIDTable('SQLite_Python.db')
        # self.weekly.create_table()
        #storage = DailyEntryStorage('SQLite_Python.db')

    @staticmethod
    def get_weekly_id():
        today = datetime.date.today()
        weekly = DateUUIDTable('SQLite_Python.db')
        weekly.create_table()
        result = weekly.find_uuid_by_date(today)
        # print(result)
        if result is None:
            # print("No weekly id exists, creating new weekly id")
            return ListBuilder.add_new_weekly()
        else:
            # print("Weekly id already exists.")
            return result

    @staticmethod
    def add_new_weekly():
        today = datetime.date.today()
        weekly = DateUUIDTable('SQLite_Python.db')
        # weekly.create_table()
        id = str(uuid.uuid4())
        weekly.add_uuid(today, id)
        return id

    def new(self):
        storage = DailyEntryStorage('SQLite_Python.db')
        weekly_id = str(self.get_weekly_id())
        new_entry = DailyEntry(uuid.uuid4(), "new2  data", datetime.datetime.now(), datetime.datetime.now(), weekly_id)
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

if __name__ == '__main__':
    list_build = ListBuilder()
    list_build.new()
    list_build.list_this_week()
    list_build.startup_weekly()
    list_build.check_for_weekly()
    print("main")
