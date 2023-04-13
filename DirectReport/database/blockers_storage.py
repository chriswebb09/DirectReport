import sqlite3
import uuid


class BlockerDataStore:

    def __init__(self, db_path):
        """
        Initializes the BlockerDataStore object with the given SQLite database file path.

        :param db_path: The SQLite database file path.
        """
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
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
                associated_entry_uuuid TEXT,
                blocker_entry TEXT
            )
        '''
        )
        self.conn.commit()

    def add_blocker_entry(self, blocker_entry, associated_entry_uuuid_str, uuid_str=None):

        if uuid_str is None:
            uuid_str = str(uuid.uuid4())
        cursor = self.conn.cursor()
        cursor.execute(
            '''
            INSERT OR IGNORE INTO blockers_uuid_table (uuid, associated_entry_uuuid, blocker_entry) VALUES (?, ?, ?)
            ''',
            (uuid_str, associated_entry_uuuid_str, blocker_entry),
        )
        self.conn.commit()

    def entries_for_associated_uuid(self, associated_uuid):

        result = self.conn.execute(
            "SELECT uuid, associated_entry_uuuid, blocker_entry FROM blockers_uuid_table WHERE associated_entry_uuuid = ?",
            (str(associated_uuid),),
        )
        return [BlockerDataStore(*row) for row in result.fetchall()]