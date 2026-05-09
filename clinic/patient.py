"""Patient module for the clinical system."""
from clinic.patient_record import PatientRecord


class Patient:
    """Represents a patient with their personal information and medical record."""
    
    def __init__(self, phn: int, name: str, birth_date: str, 
                 phone: str, email: str, address: str):
        """
        Initializes a Patient object with the provided details.
        
        Args:
            phn: Personal Health Number.
            name: Patient's full name.
            birth_date: Patient's birth date.
            phone: Patient's phone number.
            email: Patient's email address.
            address: Patient's physical address.
        """
        self.phn = phn
        self.name = name
        self.birth_date = birth_date
        self.phone = phone
        self.email = email
        self.address = address
        self.patient_record = PatientRecord(phn)

    def __eq__(self, other: object) -> bool:
        """
        Compares the current Patient object with another Patient object.
        
        Returns:
            True if all attributes (excluding patient_record) are equal.
        """
        if not isinstance(other, Patient):
            return False
        return (
            self.phn == other.phn and 
            self.name == other.name and 
            self.birth_date == other.birth_date and 
            self.phone == other.phone and 
            self.email == other.email and
            self.address == other.address
        )
