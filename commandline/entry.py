class DailyEntry:
    def __init__(self, tasks_accomplished, number_of_commits, ticket_opened, tickets_closed, day, date, week_start_date, uuid, date_created, date_last_modified):
        self.tasks_accomplished = tasks_accomplished
        self.number_of_commits = number_of_commits
        self.ticket_opened = ticket_opened
        self.ticket_closed = ticket_closed
        self.day = day
        self.date = date
        self.uuid = uuid
        self.date_created = date_created
        self.date_last_modified = date_last_modified
        
    
