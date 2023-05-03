#!/usr/bin/env python3

import sqlite3
import uuid
from pathlib import Path
import sys

file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))


class WeekUUIDTable:

    """
    A class to interact with SQLite database for managing date-UUID mappings.
    """

    def __init__(self, db_path, conn=None):
        """
        Initializes the WeekUUIDTable object with the given SQLite database file path.

        :param db_path: The SQLite database file path.
        """
        self.db_path = db_path
        if conn is None:
            self.conn = sqlite3.connect(db_path)
        else:
            self.conn = conn
        self.create_table()

    def create_table(self):
        """
        Creates the `date_uuid_table` table in the SQLite database if it doesn't exist.
        """
        cursor = self.conn.cursor()
        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS date_uuid_table (
                date TEXT PRIMARY KEY,
                uuid TEXT
            )
        '''
        )
        self.conn.commit()

    def add_uuid(self, date, uuid_str=None):
        """
        Adds a UUID for the specified date to the SQLite database.

        :param date: The date to associate with the UUID.
        :param uuid_str: The UUID string (optional). If not provided, a new UUID will be generated.
        """
        if uuid_str is None:
            uuid_str = str(uuid.uuid4())
        cursor = self.conn.cursor()
        cursor.execute(
            '''
            INSERT OR IGNORE INTO date_uuid_table (date, uuid) VALUES (?, ?)
            ''',
            (date, uuid_str),
        )
        self.conn.commit()

    def get_uuid(self, date):
        """
        Retrieves the UUID associated with the specified date.

        :param date: The date to get the associated UUID for.
        :return: The UUID string if found, otherwise `None`.
        """
        cursor = self.conn.cursor()
        cursor.execute(
            '''
            SELECT uuid FROM date_uuid_table WHERE date = ?
            ''',
            (date,),
        )
        result = cursor.fetchone()
        if result is not None:
            return result[0]
        else:
            return None

    def update_uuid(self, date, uuid_str):
        """
        Updates the UUID associated with the specified date in the SQLite database.

        :param date: The date to update the associated UUID for.
        :param uuid_str: The new UUID string.
        """
        cursor = self.conn.cursor()
        cursor.execute(
            '''
            UPDATE date_uuid_table SET uuid = ? WHERE date = ?
            ''',
            (uuid_str, date),
        )
        self.conn.commit()

    def find_uuid_by_date(self, date):
        """
        Finds the UUID associated with the specified date.

        :param date: The date to find the associated UUID for.
        :return: The UUID string if found, otherwise `None`.
        """
        cursor = self.conn.cursor()
        cursor.execute(
            '''
            SELECT uuid FROM date_uuid_table WHERE date = ?
            ''',
            (date,),
        )
        result = cursor.fetchone()
        if result is not None:
            return result[0]
        else:
            return None

    def list_all_entries(self):
        """
        Lists all date-UUID mappings from the SQLite database.

        :return: A list of tuples containing (date, UUID).
        """
        cursor = self.conn.cursor()
        cursor.execute(
            '''
            SELECT * FROM date_uuid_table
            '''
        )
        results = cursor.fetchall()
        return results

    def delete_entry_by_date(self, date):
        """
        Deletes the date-UUID mapping associated with the specified date.

        :param date: The date to delete the associated UUID for.
        """
        cursor = self.conn.cursor()
        cursor.execute(
            '''
            DELETE FROM date_uuid_table WHERE date = ?
            ''',
            (date,),
        )
        self.conn.commit()

    def delete_all_entries(self):
        """
        Deletes all entries from the database.

        :return: None
        """
        cursor = self.conn.cursor()
        cursor.execute(
            '''
            DELETE FROM date_uuid_table
            '''
        )
        self.conn.commit()
