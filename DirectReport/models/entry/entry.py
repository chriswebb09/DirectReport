#!/usr/bin/env python3

import datetime


class Entry:

    """
    A class to represent a journal entry.
    """

    def __init__(self, uuid, topic, message, created_at, modified_on):
        """
        Initialize the Entry object.
        :param uuid: A unique identifier for the entry.
        :type uuid: str
        :param topic: The topic of the entry.
        :type topic: str
        :param message: The message/content of the entry.
        :type message: str
        :param created_at: The timestamp when the entry was created.
        :type created_at: float
        :param modified_on: The timestamp when the entry was last modified.
        :type modified_on: float
        """
        self.uuid = uuid
        self.topic = topic
        self.message = message
        self.created_at = created_at
        self.modified_on = modified_on

    def get_created_at_formatted(self, date_format="%Y-%m-%d %H:%M:%S"):
        """
        Get the created_at timestamp formatted as a string.
        :param date_format: The desired format of the timestamp, default is "%Y-%m-%d %H:%M:%S".
        :type date_format: str
        :return: The formatted created_at timestamp.
        :rtype: str
        """
        return datetime.datetime.fromtimestamp(self.created_at).strftime(date_format)

    def get_modified_on_formatted(self, date_format="%Y-%m-%d %H:%M:%S"):
        """
        Get the modified_on timestamp formatted as a string.
        :param date_format: The desired format of the timestamp, default is "%Y-%m-%d %H:%M:%S".
        :type date_format: str
        :return: The formatted modified_on timestamp.
        :rtype: str
        """
        return datetime.datetime.fromtimestamp(self.modified_on).strftime(date_format)

    def to_dict(self):
        """
        Convert the Entry object to a dictionary.
        :return: The Entry object as a dictionary.
        :rtype: dict
        """
        return {
            "uuid": str(self.uuid),
            "topic": self.topic,
            "message": self.message,
            "created_at": str(self.created_at),
            "modified_on": str(self.modified_on),
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
        topic = data.get("topic")
        message = data.get("message")
        created_at = datetime.datetime.fromisoformat(data.get("created_at")).timestamp()
        modified_on = datetime.datetime.fromisoformat(data.get("modified_on")).timestamp()
        return cls(uuid, topic, message, created_at, modified_on)

    def mark_modified(self):
        """
        Update the modified_on timestamp to the current time.
        """
        self.modified_on = datetime.datetime.now().strftime("%m/%d/%Y")

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

    def set_message(self, new_message):
        """
        Update the message of the entry and set the modified_on timestamp to the current time.
        :param new_message: The new message/content for the entry.
        :type new_message: str
        """
        self.message = new_message
        self.modified_on = datetime.datetime.now().timestamp()

    def __iter__(self):
        return self

    def __str__(self):
        return "{ " + "".join((' {} : {} '.format(item, self.__dict__[item]) for item in self.__dict__)) + " }"

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self.message)
