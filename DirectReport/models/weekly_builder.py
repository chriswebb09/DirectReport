from DirectReport.database.weekly_storage import WeekUUIDTable
from DirectReport.database.entry_storage import EntryStorage
import uuid
import datetime


class WeeklyBuilder:
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
            return WeeklyBuilder.add_new_weekly()
        else:
            return result

    @staticmethod
    def week_exists():
        """
        Check if there is a week UUID associated with the current date.

        :return: True if a week UUID exists for the current date, False otherwise.
        :rtype: bool
        """
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
        if weekly.get_uuid(today) is None:
            weekly_id = str(uuid.uuid4())
            weekly.add_uuid(today, weekly_id)
            return weekly_id
        else:
            weekly_id = weekly.get_uuid(today)
            return weekly_id

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
        weekly_id = str(WeeklyBuilder.get_weekly_id())
        week_list = []
        for item in storage.get_entries_by_week(weekly_id):
            week_list.append(item.to_dict())
        return week_list
