#!/usr/bin/env python3

import datetime


class Report:

    """
    A class to represent a journal entry.
    """

    def __init__(self, uuid, user_id, raw_input, report, created_at):
        """
        Initialize the Entry object.
        :param uuid: A unique identifier for the entry.
        :type uuid: str
        :param summary: The summary of the entry.
        :type summary: str
        :param created_at: The timestamp when the entry was created.
        :type created_at: float
        """
        self.uuid = uuid
        self.user_id = user_id
        self.raw_input = raw_input
        self.report = report
        self.created_at = created_at

    def get_created_at_formatted(self, date_format="%Y-%m-%d %H:%M:%S"):
        """
        Get the created_at timestamp formatted as a string.
        :param date_format: The desired format of the timestamp, default is "%Y-%m-%d %H:%M:%S".
        :type date_format: str
        :return: The formatted created_at timestamp.
        :rtype: str
        """
        return datetime.datetime.fromtimestamp(self.created_at).strftime(date_format)

    def to_dict(self):
        """
        Convert the Entry object to a dictionary.
        :return: The Entry object as a dictionary.
        :rtype: dict
        """
        return {
            "uuid": str(self.uuid),
            "user_id": self.user_id,
            "raw_input": self.raw_input,
            "report": self.report,
            "created_at": str(self.created_at),
        }

    @classmethod
    def from_dict(cls, data):
        """
        Create an Entry object from a dictionary.
        :param data: The dictionary containing the Entry data.
        :type data: dict
        :return: An Entry object.
        :rtype: Entry
        """
        uuid = data.get("uuid")
        user_id = data.get("user_id")
        raw_input = data.get("raw_input")
        report = data.get("report")
        created_at = datetime.datetime.fromisoformat(data.get("created_at")).timestamp()
        return cls(uuid, user_id, raw_input, report, created_at)

    def is_recent(self, days=7):
        """
        Check if the entry is recent (created within the specified number of days).
        :param days: The number of days to consider as recent, default is 7.
        :type days: int
        :return: True if the entry is recent, False otherwise.
        :rtype: bool
        """
        delta = datetime.timedelta(days=days)
        difference = datetime.datetime.now() - delta
        return self.created_at >= difference.timestamp()

    def set_summary(self, report):
        """
        Update the message of the entry and set the modified_on timestamp to the current time.
        :param new_message: The new message/content for the entry.
        :type new_message: str
        """
        self.report = report

    def __iter__(self):
        return self

    def __str__(self):
        return "{ " + "".join((' {} : {} '.format(item, self.__dict__[item]) for item in self.__dict__)) + " }"

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self.report)
