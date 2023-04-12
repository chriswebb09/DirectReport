#!/usr/bin/env python3
import sqlite3

if __name__ == '__main__':
    from DirectReport.models.entry import Entry
else:
    from DirectReport.models.entry import Entry


# noinspection SqlNoDataSourceInspection
class EntryStorage:
    """
    A class to interact with SQLite database for storing and retrieving `Entry` objects.
    """

    def __init__(self, db_path):
        """
        Initializes the EntryStorage object with the given SQLite database file path.

        :param db_path: The SQLite database file path.
        """
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        """
        Creates the `entries` table in the SQLite database if it doesn't exist.
        """
        query = "CREATE TABLE IF NOT EXISTS entries (uuid TEXT PRIMARY KEY, topic TEXT, message TEXT, created_at TEXT, modified_on TEXT, week_uuid TEXT, day_uuid TEXT)"
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
            entry.day_uuid.__str__(),
        )
        self.conn.execute("INSERT INTO entries (uuid, topic, message, created_at, modified_on, week_uuid, day_uuid) VALUES (?, ?, ?, ?, ?, ?, ?)", values)
        self.conn.commit()

    def get_entry(self, uuid):
        """
        Retrieves an `Entry` object from the SQLite database by its UUID.

        :param uuid: The UUID of the entry to retrieve.
        :return: The `Entry` object if found, otherwise `None`.
        """

        result = self.conn.execute("SELECT uuid, topic, message, created_at, modified_on, week_uuid, day_uuid FROM entries WHERE uuid = ?", (str(uuid),))
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

    def get_all_entries(self):
        """
        Retrieves all `Entry` objects from the SQLite database.

        :return: A list of `Entry` objects.
        """
        result = self.conn.execute("SELECT uuid, topic, message, created_at, modified_on, week_uuid, day_uuid FROM entries")
        return [Entry(*row) for row in result.fetchall()]

    def get_all_entries_json(self):
        """
        Retrieves all `Entry` objects from the SQLite database and returns them as dictionaries.

        :return: A list of dictionaries representing `Entry` objects
        """
        result = self.conn.execute("SELECT uuid, topic, message, created_at, modified_on, week_uuid, day_uuid FROM entries")
        return [Entry(*row).to_dict() for row in result.fetchall()]

    def get_entries_by_week(self, week_uuid):
        """
        Retrieves all entries for a given week.

        :param week_uuid: The UUID of the week for which to retrieve entries.
        :return: A list of dictionaries containing the entries' data for the specified week.
        """

        result = self.conn.execute("SELECT uuid, topic, message, created_at, modified_on, week_uuid, day_uuid FROM entries WHERE week_uuid = ?", (str(week_uuid),))
        return [Entry(*row).__dict__ for row in result.fetchall()]

    def get_entries_by_day(self, day_uuid):
        """
        Retrieves all entries for a given day.

        :param day_uuid: The UUID of the day for which to retrieve entries.
        :return: A list of dictionaries containing the entries' data for the specified day.
        """

        result = self.conn.execute("SELECT uuid, topic, message, created_at, modified_on, week_uuid, day_uuid FROM entries WHERE day_uuid = ?", (str(day_uuid),))
        return [Entry(*row).__dict__ for row in result.fetchall()]

    def delete_all_entries(self):
        """
        Deletes all entries from the database.

        :return: None
        """

        self.conn.execute("DELETE FROM entries")
        self.conn.commit()


if __name__ == '__main__':
    print("main")
