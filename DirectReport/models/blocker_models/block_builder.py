#!/usr/bin/env python3


from DirectReport.database.blocker_storage import BlockerDataStore


class BlockerBuilder:
    def __init__(self):
        """
        Initializes a new instance of the BlockerBuilder class.
        """
        pass

    @staticmethod
    def add_new_blocker(blocker_text, associated_id):
        """
        Adds a new blocker entry.

        :param blocker_text: The blocker text to add.
        :param associated_id: The ID associated with the blocker entry.
        :return: None
        """
        blocker = BlockerDataStore('SQLite_Python.db')
        blocker.create_table()
        blocker.add_blocker_entry(blocker_text, str(associated_id))

    @staticmethod
    def get_blockers(associated_id):
        """
        Retrieves a list of blockers associated with the specified ID.

        :param associated_id: The ID to retrieve blockers for.
        :return: A list of blockers associated with the ID.
        """
        blockers = BlockerDataStore('SQLite_Python.db')
        blocker_list = blockers.entries_for_associated_uuid(associated_id)
        return blocker_list
