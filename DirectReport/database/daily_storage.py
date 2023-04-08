import sqlite3
import uuid


class DailyUUIDTable:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS day_uuid_table (
                date TEXT PRIMARY KEY,
                week_uuid TEXT,
                day_uuid TEXT
            )
        '''
        )
        self.conn.commit()

    def add_uuid(self, date, week_uuid_str, uuid_str=None):
        if uuid_str is None:
            uuid_str = str(uuid.uuid4())
        cursor = self.conn.cursor()
        cursor.execute(
            '''
            INSERT OR IGNORE INTO day_uuid_table (date, week_uuid, day_uuid) VALUES (?, ?, ?)
            ''',
            (date, week_uuid_str, uuid_str),
        )
        self.conn.commit()

    def get_uuid(self, date):
        cursor = self.conn.cursor()
        cursor.execute(
            '''
            SELECT day_uuid FROM day_uuid_table WHERE date = ?
            ''',
            (date,),
        )
        result = cursor.fetchone()
        if result is not None:
            return result[0]
        else:
            return None

    def update_uuid(self, date, uuid_str):
        cursor = self.conn.cursor()
        cursor.execute(
            '''
            UPDATE day_uuid_table SET day_uuid = ? WHERE date = ?
            ''',
            (uuid_str, date),
        )
        self.conn.commit()

    def find_uuid_by_date(self, date):
        cursor = self.conn.cursor()
        cursor.execute(
            '''
            SELECT day_uuid FROM day_uuid_table WHERE date = ?
            ''',
            (date,),
        )
        result = cursor.fetchone()
        if result is not None:
            return result[0]
        else:
            return None

    def list_all_entries(self):
        cursor = self.conn.cursor()
        cursor.execute(
            '''
            SELECT * FROM day_uuid_table
            '''
        )
        results = cursor.fetchall()
        return results

    def delete_entry_by_date(self, date):
        cursor = self.conn.cursor()
        cursor.execute(
            '''
            DELETE FROM day_uuid_table WHERE date = ?
            ''',
            (date,),
        )
        self.conn.commit()

    def delete_all_entries(self):
        cursor = self.conn.cursor()
        cursor.execute(
            '''
            DELETE FROM day_uuid_table
            '''
        )
        self.conn.commit()
