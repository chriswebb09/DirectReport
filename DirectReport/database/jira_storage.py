#!/usr/bin/env python3

import sqlite3
import uuid
from DirectReport.models.jira_models.jira import Jira


class JiraDataStore:
    def __init__(self, db_path, conn=None):
        """
        Initializes the JiraDataStore object with the given SQLite database file path.

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
                associated_entry_uuid TEXT,
                jira_tag TEXT,
                jira_entry
            )
        '''
        )
        self.conn.commit()

    def add_jira_entry(self, jira_tag, jira_entry, associated_entry_uuid_str, uuid_str=None):
        """
        Adds a new Jira entry to the `jiras_uuid_table`.

        :param jira_tag: The Jira tag.
        :param jira_entry: The Jira entry.
        :param associated_entry_uuid_str: The associated entry UUID as a string.
        :param uuid_str: The UUID of the Jira entry as a string (optional).
        :return: None
        """
        if uuid_str is None:
            uuid_str = str(uuid.uuid4())
        cursor = self.conn.cursor()
        cursor.execute(
            '''
            INSERT OR IGNORE INTO jiras_uuid_table (uuid, associated_entry_uuid, jira_tag, jira_entry) VALUES (?, ?, ?, ?)
            ''',
            (uuid_str, associated_entry_uuid_str, jira_tag, jira_entry),
        )
        self.conn.commit()

    def entries_for_associated_uuid(self, associated_uuid):
        """
        Retrieves a list of Jira entries associated with the specified UUID.

        :param associated_uuid: The UUID to retrieve Jira entries for.
        :return: A list of Jira entries associated with the UUID.
        """
        result = self.conn.execute(
            "SELECT uuid, associated_entry_uuid, jira_tag, jira_entry FROM jiras_uuid_table WHERE associated_entry_uuid = ?",
            (str(associated_uuid),),
        )
        return [Jira(*row).to_dict() for row in result.fetchall()]
