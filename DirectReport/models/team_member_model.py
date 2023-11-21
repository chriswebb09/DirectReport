import sqlite3
import uuid

class TeamMember:
    def __init__(self, id, team_id, username):
        self.id = id
        self.team_id = team_id
        self.username = username

class TeamMemberModel:

    def __init__(self, db_name="teammember.db"):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS teammember (
                id TEXT UNIQUE NOT NULL PRIMARY KEY,
                team_id TEXT NOT NULL,
                username TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def insert_team(self, team_id, username):
        cursor = self.conn.cursor()
        uuid_str = str(uuid.uuid4())
        try:
            cursor.execute("INSERT INTO teammember (id, team_id, username) VALUES (?, ?, ?)", (uuid_str, team_id, username))
            self.conn.commit()
            print("User added successfully!")
        except sqlite3.IntegrityError:
            print("Error: Email already exists.")

    def get_team_by_id(self, team_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, team_id, username FROM teammember WHERE team_id=?", (team_id,))
        result = cursor.fetchone()
        if result:
            return TeamMember(result[0], result[1], result[2])
    def close(self):
        self.conn.close()
