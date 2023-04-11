#!/usr/bin/env python3
import sqlite3

if __name__ == '__main__':
    from DirectReport.models.entry import Entry
else:
    from DirectReport.models.entry import Entry


class EntryStorage:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS entries (
            uuid TEXT PRIMARY KEY,
            topic TEXT,
            message TEXT,
            created_at TEXT,
            modified_on TEXT,
            week_uuid TEXT,
            day_uuid TEXT
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def add_entry(self, entry):
        query = """
        INSERT INTO entries (uuid, topic, message, created_at, modified_on, week_uuid, day_uuid)
        VALUES (?, ?, ?, ?, ?, ?, ?)
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
        self.conn.execute(query, values)
        self.conn.commit()

    def get_entry(self, uuid):
        query = """
        SELECT uuid, topic, message, created_at, modified_on, week_uuid, day_uuid
        FROM entries
        WHERE uuid = ?
        """
        result = self.conn.execute(query, (str(uuid),))
        row = result.fetchone()
        if row:
            return Entry(*row)
        else:
            return None

    def update_entry(self, entry):
        query = """
        UPDATE entries
        SET message = ?, modified_on = ?
        WHERE uuid = ?
        """
        values = (entry.message, entry.modified_on, str(entry.uuid))
        self.conn.execute(query, values)
        self.conn.commit()

    def delete_entry(self, uuid):
        query = """
        DELETE FROM entries
        WHERE uuid = ?
        """
        self.conn.execute(query, (str(uuid),))
        self.conn.commit()

    def get_all_entries(self):
        query = """
        SELECT uuid, topic, message, created_at, modified_on, week_uuid, day_uuid
        FROM entries
        """
        result = self.conn.execute(query)
        return [Entry(*row) for row in result.fetchall()]

    def get_all_entries_json(self):
        query = """
        SELECT uuid, topic, message, created_at, modified_on, week_uuid, day_uuid
        FROM entries
        """
        result = self.conn.execute(query)
        return [Entry(*row).to_dict() for row in result.fetchall()]

    def get_entries_by_week(self, week_uuid):
        query = """
        SELECT uuid, topic, message, created_at, modified_on, week_uuid, day_uuid
        FROM entries
        WHERE week_uuid = ?
        """
        result = self.conn.execute(query, (str(week_uuid),))
        return [Entry(*row).__dict__ for row in result.fetchall()]

    def get_entries_by_day(self, day_uuid):
        query = """
        SELECT uuid, topic, message, created_at, modified_on, week_uuid, day_uuid
        FROM entries
        WHERE day_uuid = ?
        """
        result = self.conn.execute(query, (str(day_uuid),))
        return [Entry(*row).__dict__ for row in result.fetchall()]

    def delete_all_entries(self):
        query = """
        DELETE FROM entries
        """
        self.conn.execute(query)
        self.conn.commit()


if __name__ == '__main__':
    print("main")
