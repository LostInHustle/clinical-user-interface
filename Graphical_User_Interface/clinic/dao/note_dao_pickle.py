import pickle
from clinic.note import *
from clinic.dao.note_dao import *

class NoteDAOPickle(NoteDAO):
    def __init__(self, number: int):
        '''
        Initializes a NoteDAOPickle instance.
        - number: Used to generate the name of the .dat file for storing notes.
        Loads existing notes from the .dat file if it exists, or creates a new .dat file if it does not.
        '''
        self.file_name = f'clinic/records/{number}.dat'
        self.note_count = 0
        self.note_list = []
        try:
            # Loads notes from the existing .dat file if it exists.
            with open(self.file_name, "rb") as file_handle:
                self.note_list = pickle.load(file_handle)
                if not self.note_list:
                    self.note_count = 0
                else:
                    self.note_count = max([note.code for note in self.note_list])
        except:
            # Creates a new .dat file if no existing file is found.
            with open(self.file_name, "wb") as file_handle:
                pickle.dump(self.note_list, file_handle)

    def create_note(self, text: str):
        '''
        Creates a new Note object, increments the note count, and saves it to the .dat file.
        - text: The content of the new note.
        Returns the created Note object.
        '''
        self.note_count += 1
        note = Note(self.note_count, text)
        self.note_list.append(note)
        with open(self.file_name, "wb") as file_handle:
            pickle.dump(self.note_list, file_handle)
        return note

    def search_note(self, key: int):
        '''
        Searches for a Note object with the specified code.
        - key: The code of the Note to search for.
        Returns the Note object if found, otherwise returns None.
        '''
        obtained_note = None
        for note in self.note_list:
            if note.code == key:
                obtained_note = note
                return obtained_note
        return obtained_note

    def retrieve_notes(self, search_string: str):
        '''
        Retrieves all Note objects containing the specified search string in their text.
        - search_string: The substring to search for within note texts.
        Returns a list of matching Note objects.
        '''
        retrieved_notes = []
        for note in self.note_list:
            if search_string in note.text:
                retrieved_notes.append(note)
        return retrieved_notes

    def update_note(self, key: int, text: str):
        '''
        Updates the text and timestamp of a Note object with the given code.
        - key: The code of the Note to update.
        - text: The new content for the Note.
        Saves the updated list to the .dat file.
        Returns True if the update was successful, otherwise returns False.
        '''
        for note in self.note_list:
            if note.code == key:
                note.text = text
                note.timestamp = datetime.now()
                with open(self.file_name, "wb") as file_handle:
                    pickle.dump(self.note_list, file_handle)
                return True
        return False

    def delete_note(self, key: int):
        '''
        Deletes the Note object with the specified code.
        - key: The code of the Note to delete.
        Saves the updated list to the .dat file.
        Returns True if the deletion was successful, otherwise returns False.
        '''
        for note in self.note_list:
            if note.code == key:
                self.note_list.remove(note)
                with open(self.file_name, "wb") as file_handle:
                    pickle.dump(self.note_list, file_handle)
                return True
        return False
    
    def list_notes(self):
        '''
        Returns all Note objects in reverse order of their creation.
        '''
        return self.note_list[::-1]