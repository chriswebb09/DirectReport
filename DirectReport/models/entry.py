#!/usr/bin/env python3
import datetime


class Entry:
    def __init__(self, uuid, topic, message, created_at, modified_on, week_uuid, day_uuid):
        self.uuid = uuid
        self.topic = topic
        self.message = message
        self.created_at = created_at
        self.modified_on = modified_on
        self.week_uuid = week_uuid
        self.day_uuid = day_uuid

    def get_created_at_formatted(self, format="%Y-%m-%d %H:%M:%S"):
        return datetime.datetime.fromtimestamp(self.created_at).strftime(format)

    def get_modified_on_formatted(self, format="%Y-%m-%d %H:%M:%S"):
        return datetime.datetime.fromtimestamp(self.modified_on).strftime(format)

    def to_dict(self):
        return {
            "uuid": str(self.uuid),
            "topic": self.topic,
            "message": self.message,
            "created_at": str(self.created_at),
            "modified_on": str(self.modified_on),
            "week_uuid": str(self.week_uuid),
            "day_uuid": str(self.day_uuid),
        }

    @classmethod
    def from_dict(cls, data):
        uuid = data.get("uuid")
        topic = data.get("topic")
        message = data.get("message")
        created_at = datetime.datetime.fromisoformat(data.get("created_at"))
        modified_on = datetime.datetime.fromisoformat(data.get("modified_on"))
        week_uuid = data.get("week_uuid")
        day_uuid = data.get("day_uuid")
        return cls(uuid, topic, message, created_at, modified_on, week_uuid, day_uuid)

    def mark_modified(self):
        self.modified_on = datetime.datetime.now()

    def is_recent(self, days=7):
        delta = datetime.timedelta(days=days)
        return self.created_at >= (datetime.datetime.now() - delta)

    def set_message(self, new_message):
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
