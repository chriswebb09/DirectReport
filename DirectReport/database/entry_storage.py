#!/usr/bin/env python3

import sqlite3
from DirectReport.models.entry import Entry


class EntryStorage:
    """
    A class to interact with SQLite database for storing and retrieving `Entry` objects.
    """

    def __init__(self, db_path, conn=None):
        """
        Initializes the EntryStorage object with the given SQLite database file path.

        :param db_path: The SQLite database file path.
        """
        if conn is None:
            self.conn = sqlite3.connect(db_path)
        else:
            self.conn = conn
        self.create_table()

    def create_table(self):
        """
        Creates the `entries` table in the SQLite database if it doesn't exist.
        """
        query = "CREATE TABLE IF NOT EXISTS entries (uuid TEXT PRIMARY KEY, topic TEXT, message TEXT, created_at TEXT, modified_on TEXT, week_uuid TEXT)"
        self.conn.execute(query)
        self.conn.commit()

    def add_entry(self, entry):
        """
        Adds an `Entry` object to the SQLite database.

        :param entry: The `Entry` object to add.
        """

        values = (
            entry.uuid.__str__(),
            entry.topic,
            entry.message,
            entry.created_at.__str__(),
            entry.modified_on.__str__(),
            entry.week_uuid.__str__(),
        )
        self.conn.execute(
            "INSERT INTO entries (uuid, topic, message, created_at, modified_on, week_uuid) VALUES (?, ?, ?, ?, ?, ?)",
            values,
        )
        self.conn.commit()

    def get_entry(self, uuid):
        """
        Retrieves an `Entry` object from the SQLite database by its UUID.

        :param uuid: The UUID of the entry to retrieve.
        :return: The `Entry` object if found, otherwise `None`.
        """

        result = self.conn.execute(
            "SELECT uuid, topic, message, created_at, modified_on, week_uuid FROM entries WHERE uuid = ?",
            (str(uuid),),
        )
        row = result.fetchone()
        if row:
            return Entry(*row)
        else:
            return None

    def update_entry(self, entry):
        """
        Updates an existing `Entry` object in the SQLite database.

        :param entry: The `Entry` object to update.
        """

        values = (entry.message, entry.modified_on, str(entry.uuid))
        self.conn.execute("UPDATE entries SET message = ?, modified_on = ? WHERE uuid = ?", values)
        self.conn.commit()

    def delete_entry(self, uuid):
        """
        Deletes an `Entry` object from the SQLite database by its UUID.

        :param uuid: The UUID of the entry to delete.
        """

        self.conn.execute("DELETE FROM entries WHERE uuid = ?", (str(uuid),))
        self.conn.commit()

    def get_entries_by_week(self, week_uuid):
        """
        Retrieves all entries for a given week.

        :param week_uuid: The UUID of the week for which to retrieve entries.
        :return: A list of dictionaries containing the entries' data for the specified week.
        """

        result = self.conn.execute(
            "SELECT uuid, topic, message, created_at, modified_on, week_uuid FROM entries WHERE week_uuid = ?",
            (str(week_uuid),),
        )
        return [Entry(*row).__dict__ for row in result.fetchall()]

    def get_uuid(self, date):
        """
        Retrieves the UUID associated with the specified date.

        :param date: The date to get the associated UUID for.
        :return: The UUID string if found, otherwise `None`.
        """
        cursor = self.conn.cursor()
        result = self.conn.execute(
            "SELECT uuid, topic, message, created_at, modified_on, week_uuid FROM entries WHERE modified_on = ?",
            (str(date),),
        )
        result = cursor.fetchone()
        if result is not None:
            return result
        else:
            return None

    def delete_all_entries(self):
        """
        Deletes all entries from the database.

        :return: None
        """

        self.conn.execute("DELETE FROM entries")
        self.conn.commit()

    def list_all_entries(self):
        """
        Lists all date-UUID mappings from the SQLite database.

        :return: A list of tuples containing (date, week_uuid, day_uuid).
        """
        cursor = self.conn.cursor()
        cursor.execute(
            '''
            SELECT * FROM entries
            '''
        )
        results = cursor.fetchall()
        return results
