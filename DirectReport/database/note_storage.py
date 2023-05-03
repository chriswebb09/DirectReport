#!/usr/bin/env python3

import sqlite3
import uuid
from DirectReport.models.note.note import Note


class NoteDataStore:
    def __init__(self, db_path, conn=None):
        """
        Initializes the NoteDataStore object with the given SQLite database file path.

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
        Creates the `note_uuid_table` table in the SQLite database if it doesn't exist.
        """
        cursor = self.conn.cursor()
        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS note_uuid_table (
                uuid TEXT PRIMARY KEY,
                associated_entry_uuid TEXT,
                note_entry TEXT
            )
        '''
        )
        self.conn.commit()

    def add_notes_entry(self, note_entry, associated_entry_uuid_str, uuid_str=None):
        """
        Adds a new note entry to the `note_uuid_table`.

        :param note_entry: The note entry.
        :param associated_entry_uuid_str: The associated entry UUID as a string.
        :param uuid_str: The UUID of the note entry as a string (optional).
        :return: None
        """
        if uuid_str is None:
            uuid_str = str(uuid.uuid4())
        cursor = self.conn.cursor()
        cursor.execute(
            '''
            INSERT OR IGNORE INTO note_uuid_table (uuid, associated_entry_uuid, note_entry) VALUES (?, ?, ?)
            ''',
            (uuid_str, associated_entry_uuid_str, note_entry),
        )
        self.conn.commit()

    def entries_for_associated_uuid(self, associated_uuid):
        """
        Retrieves a list of note entries associated with the specified UUID.

        :param associated_uuid: The UUID to retrieve note entries for.
        :return: A list of note entries associated with the UUID.
        """
        result = self.conn.execute(
            "SELECT uuid, associated_entry_uuid, note_entry FROM note_uuid_table WHERE associated_entry_uuid = ?",
            (str(associated_uuid),),
        )
        return [Note(*row).to_dict() for row in result.fetchall()]
