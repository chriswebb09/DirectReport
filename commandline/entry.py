
class DailyEntry:
    def __init__(self, uuid, message, created_at, modified_on, week_uuid):
        self.uuid = uuid
        self.message = message
        self.created_at = created_at
        self.modified_on = modified_on
        self.week_uuid = week_uuid