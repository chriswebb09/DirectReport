import sqlite3
import uuid


class Note:

    def __init__(self, uuid, associated_entry_uuid, note):
        self.uuid = uuid
        self.associated_entry_uuid = associated_entry_uuid
        self.note = note

    def to_dict(self):
        """
        Convert the Entry object to a dictionary.

        :return: The Entry object as a dictionary.
        :rtype: dict
        """

        return {
            "uuid": str(self.uuid),
            "associated_entry_uuid": str(self.associated_entry_uuid),
            "note": self.note
        }

    def __iter__(self):
        return self

    def __str__(self):
        return "{ " + "".join((' {} : {} '.format(item, self.__dict__[item]) for item in self.__dict__)) + " }"

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self.note)

class NotesDataStore:
    def __init__(self, db_path, conn=None):
        """
        Initializes the NotesDataStore object with the given SQLite database file path.

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
        TODO
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
        TODO
        """
        result = self.conn.execute(
            "SELECT uuid, associated_entry_uuid, note_entry FROM note_uuid_table WHERE associated_entry_uuid = ?",
            (str(associated_uuid),),
        )
        return [Note(*row).to_dict() for row in result.fetchall()]
