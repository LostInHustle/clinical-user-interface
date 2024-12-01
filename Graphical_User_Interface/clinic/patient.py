from clinic.patient_record import PatientRecord

class Patient:
    def __init__(self, phn: int, name: str, birth_date: str, 
                 phone: str, email: str, address: str):
        '''
        Initializes a Patient object with the provided details.
        Creates an associated PatientRecord instance for managing notes.
        '''
        self.phn = phn
        self.name = name
        self.birth_date = birth_date
        self.phone = phone
        self.email = email
        self.address = address
        self.patient_record = PatientRecord(phn)

    def __str__(self):
        '''
        Returns a string representation of the Patient object.
        Useful for printing and displaying patient details.
        '''
        return f'Patient({self.phn}, \"{self.name}\",' + ' ' + \
               f'\"{self.birth_date}\", \"{self.phone}\", \"{self.email}\",' + ' ' + \
               f'\"{self.address}\", {self.patient_record})'

    def __eq__(self, other: 'Patient'):
        '''
        Compares the current Patient object with another Patient object.
        Returns True if all attributes (excluding patient_record) are equal.
        '''
        if isinstance(other, Patient):
            return (self.phn == other.phn and 
                    self.name == other.name and 
                    self.birth_date == other.birth_date and 
                    self.phone == other.phone and 
                    self.email == other.email and
                    self.address == other.address)
        else:
            return False