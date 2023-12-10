#!/usr/bin/env python3

import datetime
import uuid
from DirectReport.models.report import Report
from DirectReport.models.report_model import ReportModel

class ReportBuilder:

    """
    A class to facilitate creating, deleting and listing entries in a weekly and daily report system.
    """

    def __init__(self):
        pass

    @staticmethod
    def new(report, raw_input, user_id):
        """
        Creates a new entry with the given entry text and topic.
        :param entry_text: The entry text.
        :param topic_text: The topic for the entry (optional).
        """
        today = datetime.date.today().strftime("%m/%d/%Y")
        storage = ReportModel('ReportStorage.db')
        storage.create_table()
        if report is None or report == '':
            report = "Entry for work on " + str(today)
        new_report = Report(
            str(uuid.uuid1()), user_id, raw_input, report, datetime.datetime.now().timestamp()
        )
        storage.add_report(new_report)

    @staticmethod
    def delete(entry_id):
        """
        Deletes an entry with the specified ID.
        :param entry_id: The ID of the entry to delete.
        """
        storage = ReportModel('ReportStorage.db')
        storage.delete_entry(entry_id)

    @staticmethod
    def get_reports_for_user_id(user_id):
        """
        Deletes an entry with the specified ID.
        :param entry_id: The ID of the entry to delete.
        """
        storage = ReportModel('ReportStorage.db')
        user_reports = storage.get_report(user_id)
        return user_reports

    @staticmethod
    def list_today():
        """
        Lists all entries for today.
        :return: A list of entries for today.
        """
        storage = ReportModel('ReportStorage.db')
        list = storage.list_all_reports()
        return list

    @staticmethod
    def list_all():
        """
        Lists all entries.
        :return: A list of all entries.
        """
        storage = ReportModel('ReportStorage.db')
        list_items = storage.list_all_reports_as_dict()
        return list_items