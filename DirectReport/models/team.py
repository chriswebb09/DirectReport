#!/usr/bin/env python3

import sqlite3
import uuid


class Team:

    def __init__(self, team_id, team_name, team_email):
        self.team_id = team_id
        self.team_name = team_name
        self.team_email = team_email
