#!/usr/bin/env python3

import sqlite3
import uuid


class TeamMember:
    def __init__(self, id, team_id, username):
        self.id = id
        self.team_id = team_id
        self.username = username
