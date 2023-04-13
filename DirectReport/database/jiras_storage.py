#!/usr/bin/env python3

import sqlite3
import uuid


class JirasDataStore:
    def __init__(self, db_path, conn=None):
        """
        Initializes the JirasDataStore object with the given SQLite database file path.

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
        Creates the `jiras_uuid_table` table in the SQLite database if it doesn't exist.
        """
        cursor = self.conn.cursor()
        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS jiras_uuid_table (
                uuid TEXT PRIMARY KEY,
                associated_entry_uuuid TEXT,
                jira_tag TEXT,
                jira_entry
            )
        '''
        )
        self.conn.commit()

    def add_jira_entry(self, jira_tag, jira_entry, associated_entry_uuuid_str, uuid_str=None):
        if uuid_str is None:
            uuid_str = str(uuid.uuid4())
        cursor = self.conn.cursor()
        cursor.execute(
            '''
            INSERT OR IGNORE INTO jiras_uuid_table (uuid, associated_entry_uuuid, jira_tag, jira_entry) VALUES (?, ?, ?, ?)
            ''',
            (uuid_str, associated_entry_uuuid_str, jira_tag, jira_entry),
        )
        self.conn.commit()

    def entries_for_associated_uuid(self, associated_uuid):
        result = self.conn.execute(
            "SELECT uuid, associated_entry_uuuid, jira_tag, jira_entry FROM jiras_uuid_table WHERE associated_entry_uuuid = ?",
            (str(associated_uuid),),
        )
        return [JirasDataStore(*row) for row in result.fetchall()]
