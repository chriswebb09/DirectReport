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

        jira = JiraDataStore('SQLite_Python.db')
        jira.create_table()
        jira.add_jira_entry(jira_tag, jira_ticket, associated_id)

    @staticmethod
    def get_jira(associated_id):
        """
        Retrieves a list of Jira associated with the specified ID.

        :param associated_id: The ID to retrieve Jira for.
        :return: A list of Jira associated with the ID.
        """

        jira = JiraDataStore('SQLite_Python.db')
        jira_list = jira.entries_for_associated_uuid(associated_id)
        return jira_list
