import sqlite3
import uuid
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, user_name, email, password):
         self.id = email
         self.user_name = user_name
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
        c = self.conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id TEXT NOT NULL,
                user_name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL PRIMARY KEY,
                password TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def insert_user(self, user_name, email, password):
        cursor = self.conn.cursor()
        uuid_str = str(uuid.uuid4())
        try:
            cursor.execute("INSERT INTO users (id, user_name, email, password) VALUES (?, ?, ?, ?)", (uuid_str, user_name, email, password))
            self.conn.commit()
            print("User added successfully!")
        except sqlite3.IntegrityError:
            print("Error: Email already exists.")

    def get_user_by_email(self, email):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, user_name, email, password FROM users WHERE email=?", (email,))
        result = cursor.fetchone()
        print(result)
        if result:
            return User(result[0], result[1], result[2], result[3])
        return None

    def get_all_users(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, user_name, email FROM users")
        return cursor.fetchall()

    def close(self):
        self.conn.close()
