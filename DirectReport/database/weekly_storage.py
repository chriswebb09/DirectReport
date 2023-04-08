#!/usr/bin/env python3

import sqlite3
import uuid


class WeekUUIDTable:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
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
        cursor = self.conn.cursor()
        cursor.execute(
            '''
            UPDATE date_uuid_table SET uuid = ? WHERE date = ?
            ''',
            (uuid_str, date),
        )
        self.conn.commit()

    def find_uuid_by_date(self, date):
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
        cursor = self.conn.cursor()
        cursor.execute(
            '''
            SELECT * FROM date_uuid_table
            '''
        )
        results = cursor.fetchall()
        return results

    def delete_entry_by_date(self, date):
        cursor = self.conn.cursor()
        cursor.execute(
            '''
            DELETE FROM date_uuid_table WHERE date = ?
            ''',
            (date,),
        )
        self.conn.commit()

    def delete_all_entries(self):
        cursor = self.conn.cursor()
        cursor.execute(
            '''
            DELETE FROM date_uuid_table
            '''
        )
        self.conn.commit()
