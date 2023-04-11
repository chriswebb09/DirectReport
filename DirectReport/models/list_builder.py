#!/usr/bin/env python3

import datetime
import sys
import uuid
from pathlib import Path

file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))

if __name__ == '__main__':
    from ..database.daily_storage import DailyUUIDTable
    from ..database.weekly_storage import WeekUUIDTable
    from ..database.entry_storage import EntryStorage
    from ..models.entry import Entry
else:
    from DirectReport.database.daily_storage import DailyUUIDTable
    from DirectReport.database.weekly_storage import WeekUUIDTable
    from DirectReport.database.entry_storage import EntryStorage
    from DirectReport.models.entry import Entry


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
    def get_daily_id():
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
        today = datetime.date.today().strftime("%m/%d/%Y, %H:%M:%S")
        weekly = WeekUUIDTable('SQLite_Python.db')
        id = str(uuid.uuid4())
        weekly.add_uuid(today, id)
        return id

    @staticmethod
    def add_new_daily():
        today = datetime.date.today().strftime("%m/%d/%Y, %H:%M:%S")
        daily = DailyUUIDTable('SQLite_Python.db')
        daily.create_table()
        weekly_id = str(ListBuilder.get_weekly_id())
        daily_id = str(uuid.uuid4())
        daily.add_uuid(str(today), weekly_id, daily_id)
        return daily_id

    @staticmethod
    def new(entry, topic=None):
        storage = EntryStorage('SQLite_Python.db')
        weekly_id = str(ListBuilder.get_weekly_id())
        daily_id = str(ListBuilder.get_daily_id())
        if topic is None:
            topic = "Entry for work on " + str(datetime.datetime.now().strftime("%b %d, %Y"))

        new_entry = Entry(
            uuid.uuid4(), topic, entry, datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), weekly_id, daily_id
        )
        storage.add_entry(new_entry)

    @staticmethod
    def delete(id):
        storage = EntryStorage('SQLite_Python.db')
        storage.delete_entry(id)

    @staticmethod
    def list_all_daily_ids():
        storage = DailyUUIDTable('SQLite_Python.db')
        list_all = storage.list_all_entries()
        return list_all

    @staticmethod
    def list_all_week_ids():
        storage = WeekUUIDTable('SQLite_Python.db')
        list_all = storage.list_all_entries()
        return list_all

    @staticmethod
    def list_today():
        storage = EntryStorage('SQLite_Python.db')
        daily_id = str(ListBuilder.get_daily_id())
        daily_list = storage.get_entries_by_day(daily_id)
        return daily_list

    @staticmethod
    def list_this_week():
        storage = EntryStorage('SQLite_Python.db')
        weekly_id = str(ListBuilder.get_weekly_id())
        week_list = storage.get_entries_by_week(weekly_id)
        return week_list

    @staticmethod
    def list_week(weekly_id):
        storage = EntryStorage('SQLite_Python.db')
        weekly_id = str(weekly_id)
        week_list = storage.get_entries_by_week(weekly_id)
        return week_list

    @staticmethod
    def list_all():
        storage = EntryStorage('SQLite_Python.db')
        list = storage.get_all_entries()
        return list

    @staticmethod
    def list_this_week_as_json():
        storage = EntryStorage('SQLite_Python.db')
        weekly_id = str(ListBuilder.get_weekly_id())
        week_list = []
        for item in storage.get_entries_by_week(weekly_id):
            week_list.append(item.to_dict())
        return week_list


if __name__ == '__main__':
    print("main")
