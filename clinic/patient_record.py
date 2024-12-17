from clinic.dao.note_dao_pickle import *

class PatientRecord:
    def __init__(self, number: int):
        '''
        Initializes a PatientRecord object for a patient.
        This includes a NoteDAOPickle instance to manage notes.
        note_count tracks the total number of notes, starting at 1 for the first note.
        '''
        self.note_dao = NoteDAOPickle(number)
    
    def create_note(self, text: str):
        '''
        Creates a new Note object with the given text and adds it to the patient's record.
        Increments note_count for each new note.
        '''
        return self.note_dao.create_note(text)
    
    def search_note(self, num: int):
        '''
        Searches for and returns a Note object with the specified code.
        Returns None if no note with the given code is found.
        '''
        return self.note_dao.search_note(num)
    
    def retrieve_notes(self, txt: str):
        '''
        Retrieves all Note objects that contain the given text.
        Returns an empty list if no matching notes are found.
        '''
        return self.note_dao.retrieve_notes(txt)
    
    def update_note(self, code: int, text: str):
        '''
        Updates the text of the Note object with the specified code.
        Also updates the note's timestamp to the current date and time.
        '''
        return self.note_dao.update_note(code, text)
    
    def delete_note(self, code: int):
        '''
        Deletes the Note object with the specified code from the record.
        Returns False if no note with the given code exists.
        '''
        return self.note_dao.delete_note(code)
    
    def list_notes(self):
        '''
        Returns a list of all Note objects in the record.
        Notes are returned in the order they were added.
        '''
        return self.note_dao.list_notes()
