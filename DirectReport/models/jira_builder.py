from DirectReport.database.jira_storage import JiraDataStore


class JiraBuilder:
    def __init__(self):
        pass

    @staticmethod
    def add_new_jira(jira_ticket, jira_tag, associated_id):
        """
        Adds a new daily ID.

        :return: The newly created daily ID.
        """

        jiras = JiraDataStore('SQLite_Python.db')
        jiras.create_table()
        jiras.add_jira_entry(jira_tag, jira_ticket, associated_id)

    @staticmethod
    def get_jiras(associated_id):
        """
        TODO
        """

        jiras = JiraDataStore('SQLite_Python.db')
        jiras_list = jiras.entries_for_associated_uuid(associated_id)
        print(jiras_list)
        return jiras_list
