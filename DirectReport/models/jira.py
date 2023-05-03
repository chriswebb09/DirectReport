#!/usr/bin/env python3


class Jira:

    def __init__(self, uuid, associated_entry_uuid, jira_tag, jira_ticket):
        self.uuid = uuid
        self.associated_entry_uuid = associated_entry_uuid
        self.jira_tag = jira_tag
        self.jira_ticket = jira_ticket

    def to_dict(self):
        """
        Convert the Entry object to a dictionary.

        :return: The Entry object as a dictionary.
        :rtype: dict
        """

        return {
            "uuid": str(self.uuid),
            "associated_entry_uuid": str(self.associated_entry_uuid),
            "jira_tag": self.jira_tag,
            "jira_ticket": self.jira_ticket,
        }

    def __iter__(self):
        return self

    def __str__(self):
        return "{ " + "".join((' {} : {} '.format(item, self.__dict__[item]) for item in self.__dict__)) + " }"

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self.jira_ticket)
