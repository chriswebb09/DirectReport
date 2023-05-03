#!/usr/bin/env python3


class Blocker:
    def __init__(self, uuid, associated_entry_uuid, blocker_text):
        """
        Initializes a new instance of the Blocker class.

        :param uuid: The UUID of the blocker.
        :param associated_entry_uuid: The UUID of the associated entry.
        :param blocker_text: The blocker text.
        """
        self.uuid = uuid
        self.associated_entry_uuid = associated_entry_uuid
        self.blocker_text = blocker_text

    def to_dict(self):
        """
        Convert the Blocker object to a dictionary.

        :return: The Blocker object as a dictionary.
        :rtype: dict
        """
        return {
            "uuid": str(self.uuid),
            "associated_entry_uuid": str(self.associated_entry_uuid),
            "blocker_models": self.blocker_text,
        }

    def __iter__(self):
        return self

    def __str__(self):
        return "{ " + "".join((' {} : {} '.format(item, self.__dict__[item]) for item in self.__dict__)) + " }"

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self.blocker_text)
