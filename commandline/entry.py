import datetime
class DailyEntry:
    def __init__(self, uuid, message, created_at, modified_on, week_uuid):
        self.uuid = uuid
        self.message = message
        self.created_at = created_at
        self.modified_on = modified_on
        self.week_uuid = week_uuid

    def get_created_at_formatted(self, format="%Y-%m-%d %H:%M:%S"):
        return datetime.datetime.fromtimestamp(self.created_at).strftime(format)

    def get_modified_on_formatted(self, format="%Y-%m-%d %H:%M:%S"):
        return datetime.datetime.fromtimestamp(self.modified_on).strftime(format)

    def to_dict(self):
        return {
            "uuid": self.uuid,
            "message": self.message,
            "created_at": self.created_at.isoformat(),
            "modified_on": self.modified_on.isoformat(),
            "week_uuid": self.week_uuid
        }

    @classmethod
    def from_dict(cls, data):
        uuid = data.get("uuid")
        message = data.get("message")
        created_at = datetime.datetime.fromisoformat(data.get("created_at"))
        modified_on = datetime.datetime.fromisoformat(data.get("modified_on"))
        week_uuid = data.get("week_uuid")
        return cls(uuid, message, created_at, modified_on, week_uuid)

    def mark_modified(self):
        self.modified_on = datetime.datetime.now()

    def is_recent(self, days=7):
        delta = datetime.timedelta(days=days)
        return self.created_at >= (datetime.datetime.now() - delta)

    def set_message(self, new_message):
        self.message = new_message
        self.modified_on = datetime.datetime.now().timestamp()

    def __str__(self):
        return  str(self.__class__) + '\n'+ '\n'.join(('{} = {}'.format(item, self.__dict__[item]) for item in self.__dict__))
        # return f"DailyEntry(uuid={self.uuid}, message='{self.message}', created_at={self.created_at}, modified_on={self.modified_on}, week_uuid={self.week_uuid})"

    def __len__(self):
        return len(self.message)