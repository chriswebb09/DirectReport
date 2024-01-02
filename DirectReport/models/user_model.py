#!/usr/bin/env python3

import sqlite3
import uuid
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin):
    def __init__(self, id, username, firstname, lastname, email, password, github_username):
        self.id = email
        self.uid = id
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.authenticated = True
        self.github_username = github_username

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return self.authenticated

    def get_id(self):
        return self.id

    def check_password(self, password):
        return check_password_hash(self.password, password)


class UserModel:
    def __init__(self, db_name="users.db"):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id TEXT NOT NULL,
                uid TEXT NOT NULL,
                username TEXT NOT NULL,
                firstname TEXT NOT NULL,
                lastname TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL PRIMARY KEY,
                password TEXT NOT NULL,
                github_username TEXT NOT NULL
            )
        """
        )
        self.conn.commit()

    def insert_user(self, id, username, firstname, lastname, email, password):
        cursor = self.conn.cursor()
        uuid_str = str(uuid.uuid4())
        gitub_username = ""
        try:
            cursor.execute(
                "INSERT INTO users (id, uid, username, firstname, lastname, email, password, github_username) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (id, uuid_str, username, firstname, lastname, email, password, gitub_username),
            )
            self.conn.commit()
            print("User added successfully!")
        except sqlite3.IntegrityError:
            print("Error: Email already exists.")

    def get_user_by_email(self, email):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT id, uid, username, firstname, lastname, email, password, github_username FROM users WHERE email=?",
            (email,),
        )
        result = cursor.fetchone()
        if result:
            return User(result[0], result[2], result[3], result[4], result[5], result[6], result[7])
        return None

    def update_github_username(self, email, new_github_username):
        cursor = self.conn.cursor()
        try:
            cursor.execute("UPDATE users SET github_username = ? WHERE email = ?", (new_github_username, email))
            self.conn.commit()
            if cursor.rowcount == 0:
                print("No user found with the given email.")
            else:
                print("GitHub username updated successfully!")
        except sqlite3.Error as e:
            print("An error occurred:", e)

    def get_all_users(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, uid, username, firstname, lastname, email FROM users")
        return cursor.fetchall()

    def close(self):
        self.conn.close()
