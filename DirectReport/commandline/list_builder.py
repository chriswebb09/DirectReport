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

    def get_weekly_id(self):
        today = datetime.date.today()
        weekly = DateUUIDTable('SQLite_Python.db')
        weekly.create_table()
        result = weekly.find_uuid_by_date(str(today))
        print(result)
        if result is None:
            print("No weekly id exists, creating new weekly id")
            return uuid.uuid4()
        else:
            print("Weekly id already exists.")
            return result

    def startup_weekly(self):
        today = datetime.date.today()
        weekly = DateUUIDTable('SQLite_Python.db')
        weekly.create_table()
        weekly.add_uuid(today)

    def new(self):
        storage = DailyEntryStorage('SQLite_Python.db')
        weekly_id = str(self.get_weekly_id())
        new_entry = DailyEntry(uuid.uuid4(), "new2  data", datetime.datetime.now(), datetime.datetime.now(), weekly_id)
        storage.add_entry(new_entry)

    def list_this_week(self):
        storage = DailyEntryStorage('SQLite_Python.db')
        weekly_id = str(self.get_weekly_id())
        print(weekly_id)
        list = storage.get_entries_by_week(weekly_id)
            # storage.get_entries_by_week(weekly_id)
        for item in list:
            print(item)
            print("")

        list_all = storage.get_all_entries()
        for list_item in list_all:
            print(list_item)
            print("")

if __name__ == '__main__':
    list_build = ListBuilder()
    list_build.new()
    list_build.list_this_week()
    # list_build.startup_weekly()
    # list_build.check_for_weekly()
    print("main")
