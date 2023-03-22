#!/usr/bin/env python3
import sqlite3

if __name__ == '__main__':
    from .entry import DailyEntry
else:
    from entry import DailyEntry



class DailyEntryStorage:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS daily_entries (
            uuid TEXT PRIMARY KEY,
            message TEXT,
            created_at TEXT,
            modified_on TEXT,
            week_uuid TEXT
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def add_entry(self, entry):
        query = """
        INSERT INTO daily_entries (uuid, message, created_at, modified_on, week_uuid)
        VALUES (?, ?, ?, ?, ?)
        """
        values = (
            entry.uuid.__str__(),
            entry.message,
            entry.created_at.__str__(),
            entry.modified_on.__str__(),
            entry.week_uuid.__str__(),
        )
        self.conn.execute(query, values)
        self.conn.commit()

    def get_entry(self, uuid):
        query = """
        SELECT uuid, message, created_at, modified_on, week_uuid
        FROM daily_entries
        WHERE uuid = ?
        """
        result = self.conn.execute(query, (uuid,))
        row = result.fetchone()
        if row:
            return DailyEntry(*row)
        else:
            return None

    def update_entry(self, entry):
        query = """
        UPDATE daily_entries
        SET message = ?, modified_on = ?
        WHERE uuid = ?
        """
        values = (entry.message, entry.modified_on, entry.uuid)
        self.conn.execute(query, values)
        self.conn.commit()

    def delete_entry(self, uuid):
        query = """
        DELETE FROM daily_entries
        WHERE uuid = ?
        """
        self.conn.execute(query, (uuid,))
        self.conn.commit()

    def get_all_entries(self):
        query = """
        SELECT uuid, message, created_at, modified_on, week_uuid
        FROM daily_entries
        """
        result = self.conn.execute(query)
        return [DailyEntry(*row) for row in result.fetchall()]

    def get_entries_by_week(self, week_uuid):
        query = """
        SELECT uuid, message, created_at, modified_on, week_uuid
        FROM daily_entries
        WHERE week_uuid = ?
        """
        result = self.conn.execute(query, (week_uuid,))
        return [DailyEntry(*row) for row in result.fetchall()]


if __name__ == '__main__':
    print("main")
