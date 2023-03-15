#!/usr/bin/env python3

import sqlite3


class DataStorage:
    def connect_DB(self):
        try:
            self.sqliteConnection = sqlite3.connect('SQLite_Python.db')
            cursor = self.sqliteConnection.cursor()
            print("Database created and Successfully Connected to SQLite")
            sqlite_select_Query = "select sqlite_version();"
            cursor.execute(sqlite_select_Query)
            record = cursor.fetchall()
            print("SQLite Database Version is: ", record)
            cursor.close()
        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)
        finally:
            if self.sqliteConnection:
                self.sqliteConnection.close()
                print("The SQLite connection is closed")
