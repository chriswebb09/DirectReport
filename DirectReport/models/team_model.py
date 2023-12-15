#!/usr/bin/env python3

import sqlite3
import uuid


class TeamModel:
    def __init__(self, db_name="team.db"):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute(
            """ 
            CREATE TABLE IF NOT EXISTS team (
                id TEXT UNIQUE NOT NULL PRIMARY KEY,
                team_name TEXT NOT NULL,
                team_email TEXT NOT NULL
            )
        """
        )

    def insert_team(self, team_name, team_email):
        cursor = self.conn.cursor()
        uuid_str = str(uuid.uuid4())
        try:
            cursor.execute(
                "INSERT INTO team (id, team_name, team_email) VALUES (?, ?, ?)", (uuid_str, team_name, team_email)
            )
            self.conn.commit()
            print("User added successfully!")
        except sqlite3.IntegrityError:
            print("Error: Email already exists.")

    def get_team_by_email(self, team_email):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, team_name, team_email, password FROM team WHERE team_email=?", (team_email,))
        result = cursor.fetchone()
        if result:
            return Team(result[0], result[1], result[2])
        return None

    def close(self):
        self.conn.close()
