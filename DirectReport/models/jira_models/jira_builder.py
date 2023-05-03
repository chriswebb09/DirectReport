#!/usr/bin/env python3

from DirectReport.database.jira_storage import JiraDataStore


class JiraBuilder:
    def __init__(self):
        pass

    @staticmethod
    def add_new_jira(jira_ticket, jira_tag, associated_id):
        """
        Adds a new Jira entry to the list.

        :param jira_ticket: The Jira ticket to add.
        :param jira_tag: The Jira tag associated with the ticket.
        :param associated_id: The ID associated with the Jira entry.
        :return: None
        """

        jiras = JiraDataStore('SQLite_Python.db')
        jiras.create_table()
        jiras.add_jira_entry(jira_tag, jira_ticket, associated_id)

    @staticmethod
    def get_jiras(associated_id):
        """
        Retrieves a list of Jiras associated with the specified ID.

        :param associated_id: The ID to retrieve Jiras for.
        :return: A list of Jiras associated with the ID.
        """

        jiras = JiraDataStore('SQLite_Python.db')
        jiras_list = jiras.entries_for_associated_uuid(associated_id)
        return jiras_list
