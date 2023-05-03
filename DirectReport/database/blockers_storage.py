#!/usr/bin/env python3

import sqlite3
import uuid

class Blocker:

    def __init__(self, uuid, associated_entry_uuid, blocker_text):
        self.uuid = uuid
        self.associated_entry_uuid = associated_entry_uuid
        self.blocker_text = blocker_text

    def to_dict(self):
        """
        Convert the Entry object to a dictionary.

        :return: The Entry object as a dictionary.
        :rtype: dict
        """

        return {
            "uuid": str(self.uuid),
            "associated_entry_uuid": str(self.associated_entry_uuid),
            "blocker": self.blocker_text
        }

    def __iter__(self):
        return self

    def __str__(self):
        return "{ " + "".join((' {} : {} '.format(item, self.__dict__[item]) for item in self.__dict__)) + " }"

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self.blocker_text)

class BlockerDataStore:
    def __init__(self, db_path, conn=None):
        """
        Initializes the BlockerDataStore object with the given SQLite database file path.

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
        Creates the `blockers_uuid_table` table in the SQLite database if it doesn't exist.
        """
        cursor = self.conn.cursor()
        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS blockers_uuid_table (
                uuid TEXT PRIMARY KEY,
                associated_entry_uuid TEXT,
                blocker_entry TEXT
            )
        '''
        )
        self.conn.commit()

    def add_blocker_entry(self, blocker, associated_entry_uuid_str, uuid_str=None):
        """
        TODO
        """
        if uuid_str is None:
            uuid_str = str(uuid.uuid4())
        cursor = self.conn.cursor()
        cursor.execute(
            '''
            INSERT OR IGNORE INTO blockers_uuid_table (uuid, associated_entry_uuid, blocker_entry) VALUES (?, ?, ?)
            ''',
            (uuid_str, associated_entry_uuid_str, blocker),
        )
        self.conn.commit()

    def entries_for_associated_uuid(self, associated_uuid):
        """
        TODO
        """
        result = self.conn.execute(
            "SELECT uuid, associated_entry_uuid, blocker_entry FROM blockers_uuid_table WHERE associated_entry_uuid = ?",
            (str(associated_uuid),),
        )
        return [Blocker(*row).to_dict() for row in result.fetchall()]
