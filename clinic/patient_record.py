"""PatientRecord module for managing patient medical notes."""
from clinic.dao.note_dao_pickle import NoteDAOPickle


class PatientRecord:
    """Manages a patient's medical records including notes."""
    
    def __init__(self, number: int):
        """
        Initializes a PatientRecord object for a patient.
        
        Args:
            number: Patient's PHN used to generate the note storage file name.
        """
        self.note_dao = NoteDAOPickle(number)
    
    def create_note(self, text: str) -> 'Note':
        """
        Creates a new Note with the given text and adds it to the patient's record.
        
        Args:
            text: The content of the new note.
        Returns:
            The created Note object.
        """
        return self.note_dao.create_note(text)
    
    def search_note(self, num: int) -> 'Note':
        """
        Searches for a Note with the specified code.
        
        Args:
            num: The code of the Note to search for.
        Returns:
            The Note object if found, otherwise None.
        """
        return self.note_dao.search_note(num)
    
    def retrieve_notes(self, txt: str) -> list:
        """
        Retrieves all Notes that contain the given text.
        
        Args:
            txt: Substring to search for in note texts.
        Returns:
            A list of matching Note objects.
        """
        return self.note_dao.retrieve_notes(txt)
    
    def update_note(self, code: int, text: str) -> bool:
        """
        Updates the text of the Note with the specified code.
        
        Args:
            code: The code of the Note to update.
            text: The new content for the Note.
        Returns:
            True if the update was successful.
        """
        return self.note_dao.update_note(code, text)
    
    def delete_note(self, code: int) -> bool:
        """
        Deletes the Note with the specified code from the record.
        
        Args:
            code: The code of the Note to delete.
        Returns:
            True if the deletion was successful, False otherwise.
        """
        return self.note_dao.delete_note(code)
    
    def list_notes(self) -> list:
        """
        Returns a list of all Notes in the record (in reverse order).
        
        Returns:
            List of Note objects.
        """
        return self.note_dao.list_notes()
