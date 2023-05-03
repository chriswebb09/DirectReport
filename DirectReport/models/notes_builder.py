#!/usr/bin/env python3

from ..database.notes_storage import NotesDataStore


class NotesBuilder:
    def __init__(self):
        pass

    @staticmethod
    def add_new_note(note_text, associated_id):
        """
        Adds a new daily ID.

        :return: The newly created daily ID.
        """

        notes = NotesDataStore('SQLite_Python.db')
        notes.add_notes_entry(note_text, associated_id)

    @staticmethod
    def get_notes(associated_id):
        """
        TODO
        """

        notes = NotesDataStore('SQLite_Python.db')
        note_list = notes.entries_for_associated_uuid(associated_id)
        return note_list
