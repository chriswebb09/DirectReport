#!/usr/bin/env python3

import datetime
from DirectReport.database.daily_storage import DailyUUIDTable
import DirectReport.models.weekly_builder as WeeklyBuilder
import uuid


class DailyBuilder:
    def __init__(self):
        pass

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
            return DailyBuilder.add_new_daily()
        else:
            return result

    @staticmethod
    def add_new_daily():
        """
        Adds a new daily ID.

        :return: The newly created daily ID.
        """
        today = datetime.date.today().strftime("%m/%d/%Y")
        daily = DailyUUIDTable('SQLite_Python.db')
        daily.create_table()
        weekly_id = str(WeeklyBuilder.get_weekly_id())
        if daily.get_uuid(today) is not None:
            daily_id = daily.get_uuid(today)
            return daily_id
        else:
            daily_id = str(uuid.uuid4())
            daily.add_uuid(str(today), weekly_id, daily_id)
            return daily_id

    @staticmethod
    def list_all_daily_ids():
        """
        Lists all daily IDs.

        :return: A list of all daily IDs.
        """
        storage = DailyUUIDTable('SQLite_Python.db')
        list_all = storage.list_all_entries()
        return list_all
