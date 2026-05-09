"""Note module for the clinical system."""
from datetime import datetime


class Note:
    """Represents a medical note with content and timestamp."""
    
    def __init__(self, code: int, text: str):
        """
        Initializes a Note object with a unique code, text content, and a timestamp.
        
        Args:
            code: A unique identifier assigned in sequential order.
            text: The content of the note.
        """
        self.code = code
        self.text = text
        self.timestamp = datetime.now()

    def update_time(self) -> None:
        """Updates the timestamp to the current date and time."""
        self.timestamp = datetime.now()
    
    def __eq__(self, other: object) -> bool:
        """
        Checks if two Note objects are equal.
        
        Returns:
            True if both the code and text of the notes match.
        """
        if not isinstance(other, Note):
            return False
        return self.code == other.code and self.text == other.text
