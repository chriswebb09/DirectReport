#!/usr/bin/env python3

import sqlite3
import uuid

class Jira:

    def __init__(self, uuid, associated_entry_uuid, jira_tag, jira_ticket):
        self.uuid = uuid
        self.associated_entry_uuid = associated_entry_uuid
        self.jira_tag = jira_tag
        self.jira_ticket = jira_ticket


    def to_dict(self):
        """
        Convert the Entry object to a dictionary.

        :return: The Entry object as a dictionary.
        :rtype: dict
        """

        return {
            "uuid": str(self.uuid),
            "associated_entry_uuid": str(self.associated_entry_uuid),
            "jira_tag": self.jira_tag,
            "jira_ticket": self.jira_ticket
        }

    def __iter__(self):
        return self

    def __str__(self):
        return "{ " + "".join((' {} : {} '.format(item, self.__dict__[item]) for item in self.__dict__)) + " }"

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self.jira_ticket)

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
                associated_entry_uuid TEXT,
                jira_tag TEXT,
                jira_entry
            )
        '''
        )
        self.conn.commit()

    def add_jira_entry(self, jira_tag, jira_entry, associated_entry_uuid_str, uuid_str=None):
        """
        TODO
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
        TODO
        """
        result = self.conn.execute(
            "SELECT uuid, associated_entry_uuid, jira_tag, jira_entry FROM jiras_uuid_table WHERE associated_entry_uuid = ?",
            (str(associated_uuid),),
        )
        return [Jira(*row).to_dict() for row in result.fetchall()]
