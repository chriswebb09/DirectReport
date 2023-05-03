from DirectReport.database.blockers_storage import BlockerDataStore


class BlockersBuilder:
    def __init__(self):
        pass

    @staticmethod
    def add_new_blocker(blocker_text, associated_id):
        """
        Adds a new daily ID.

        :return: The newly created daily ID.
        """

        blocker = BlockerDataStore('SQLite_Python.db')
        blocker.create_table()
        blocker.add_blocker_entry(blocker_text, str(associated_id))

    @staticmethod
    def get_blockers(associated_id):
        """
        TODO
        """

        blockers = BlockerDataStore('SQLite_Python.db')
        blocker_list = blockers.entries_for_associated_uuid(associated_id)
        print(blocker_list)
        return blocker_list
