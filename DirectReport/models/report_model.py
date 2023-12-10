import sqlite3
from DirectReport.models.report import Report

class ReportModel:
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
        query = "CREATE TABLE IF NOT EXISTS reports (uuid TEXT PRIMARY KEY, summary TEXT,created_at TEXT)"
        self.conn.execute(query)
        self.conn.commit()

    def add_report(self, entry):
        """
        Adds an `Entry` object to the SQLite database.
        :param entry: The `Entry` object to add.
        """

        values = (
            entry.uuid.__str__(),
            entry.summary,
            entry.created_at.__str__()
        )
        self.conn.execute(
            "INSERT OR IGNORE INTO reports (uuid, summary, created_at) VALUES (?, ?, ?)",
            values,
        )
        self.conn.commit()

    def get_report(self, uuid):
        """
        Retrieves an `Entry` object from the SQLite database by its UUID.
        :param uuid: The UUID of the entry to retrieve.
        :return: The `Entry` object if found, otherwise `None`.
        """

        result = self.conn.execute(
            "SELECT uuid, summary, created_at FROM reports WHERE uuid = ?",
            (str(uuid),),
        )
        row = result.fetchone()
        if row:
            return Report(*row)
        else:
            return None

    # def update_entry(self, entry):
    #     """
    #     Updates an existing `Entry` object in the SQLite database.
    #     :param entry: The `Entry` object to update.
    #     """
    #
    #     values = (entry.message, entry.modified_on, str(entry.uuid))
    #     self.conn.execute("UPDATE entries SET message = ?, modified_on = ? WHERE uuid = ?", values)
    #     self.conn.commit()

    def delete_entry(self, uuid):
        """
        Deletes an `Entry` object from the SQLite database by its UUID.
        :param uuid: The UUID of the entry to delete.
        """

        self.conn.execute("DELETE FROM reports WHERE uuid = ?", (str(uuid),))
        self.conn.commit()

    def get_uuid(self, date):
        """
        Retrieves the UUID associated with the specified date.
        :param date: The date to get the associated UUID for.
        :return: The UUID string if found, otherwise `None`.
        """

        result = self.conn.execute(
            "SELECT uuid, summary, created_at FROM reports WHERE modified_on = ?",
            (str(date),),
        )
        if result is not None:
            return result.fetchone()
        else:
            return None

    def delete_all_reports(self):
        """
        Deletes all entries from the database.
        :return: None
        """

        self.conn.execute("DELETE FROM reports")
        self.conn.commit()

    def list_all_reports_as_dict(self):
        """
        Lists all date-UUID mappings from the SQLite database.
        :return: A list of tuples containing (date, week_uuid, day_uuid).
        """
        cursor = self.conn.cursor()
        cursor.execute(
            '''
            SELECT * FROM reports
            '''
        )
        results = cursor.fetchall()

        results_list = []
        for result in results:
            entry = Entry(*result)
            entry_dict = entry.to_dict()
            results_list.append(entry_dict)
        return results_list

    def list_all_reports(self):
        """
        Lists all date-UUID mappings from the SQLite database.
        :return: A list of tuples containing (date, week_uuid, day_uuid).
        """
        cursor = self.conn.cursor()
        cursor.execute(
            '''
            SELECT * FROM reports
            '''
        )
        results = cursor.fetchall()
        return results
