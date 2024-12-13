from datetime import datetime

class Note:
    def __init__(self: 'Note', code: int, text: str):
        '''
        Initializes a Note object with a unique code, text content, and a timestamp.
        - code: A unique identifier assigned in sequential order.
        - text: The content of the note.
        - timestamp: The date and time when the note is created, automatically set to the current time.
        '''
        self.code = code
        self.text = text
        self.timestamp = datetime.now()

    def update_time(self: 'Note'):
        '''
        Updates the timestamp to the current date and time.
        Useful when the note's content is modified.
        '''
        self.timestamp = datetime.now()

    def __str__(self: 'Note'):
        '''
        Returns a string representation of the Note object.
        Useful for printing or displaying the note's details.
        '''
        return f'Note({self.code}, \"{self.text}\", \"{self.timestamp}\")'
    
    def __repr__(self: 'Note'):
        '''
        Returns the official string representation of the Note object.
        This is the same as the __str__ method for consistency.
        '''
        return str(self)
    
    def __eq__(self: 'Note', other_note: 'Note'):
        '''
        Checks if two Note objects are equal.
        Returns True if both the code and text of the notes match.
        '''
        if not isinstance(other_note, Note):
            return False
        check_code = (self.code == other_note.code)
        check_text = (self.text == other_note.text)
        return (check_code and check_text)