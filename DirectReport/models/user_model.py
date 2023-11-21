import sqlite3
import uuid
from flask_login import UserMixin
from app import app as application
class User(UserMixin):

    def __init__(self, id, username, email, password):
        self.id = email
        self.uid = id
        self.username = username
        self.email = email
        self.password = password
        self.authenticated = True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return self.authenticated

    def is_active(self):
        return True

    def get_id(self):
        return self.id

class UserModel:
    def __init__(self, db_name="users.db"):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id TEXT NOT NULL,
                username TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL PRIMARY KEY,
                password TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def insert_user(self, username, email, password):
        cursor = self.conn.cursor()
        uuid_str = str(uuid.uuid4())
        try:
            cursor.execute("INSERT INTO users (id, username, email, password) VALUES (?, ?, ?, ?)", (uuid_str, username, email, password))
            self.conn.commit()
            print("User added successfully!")
        except sqlite3.IntegrityError:
            print("Error: Email already exists.")

    def get_user_by_email(self, email):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, username, email, password FROM users WHERE email=?", (email,))
        result = cursor.fetchone()
        if result:
            return User(result[0], result[1], result[2], result[3])
        return None

    def get_all_users(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, username, email FROM users")
        return cursor.fetchall()

    def close(self):
        self.conn.close()
