# Import necessary modules and classes.
from clinic.patient_record import *
from clinic.dao.patient_dao_json import *
from clinic.exception.invalid_login_exception import InvalidLoginException
from clinic.exception.duplicate_login_exception import DuplicateLoginException
from clinic.exception.invalid_logout_exception import InvalidLogoutException
from clinic.exception.illegal_access_exception import IllegalAccessException
from clinic.exception.illegal_operation_exception import IllegalOperationException
from clinic.exception.no_current_patient_exception import NoCurrentPatientException
# Used for password hashing.
import hashlib

class Controller:
    def __init__(self, autosave: bool = False):
        '''
        Initializes a Controller object.
        This manages patient records and user authentication.
        '''
        self.logged_in = False
        self.autosave = autosave
        self.patient_dao = PatientDAOJSON(autosave)
        self.current_patient = None
    
    def get_password_hash(self, password: str):
        '''
        Returns the SHA-256 hash of the given password string.
        Used to securely store and compare passwords.
        '''
        password = password.encode('utf-8')
        password = hashlib.sha256(password)
        new_password = password.hexdigest()
        return new_password

    def login(self, username: str, password: str):
        '''
        Authenticates the user with the given username and password.
        If successful, sets self.logged_in to True. Raises InvalidLoginException
        if credentials are incorrect and DuplicateLoginException if already logged in.
        '''
        user_list = []
        password_list = []
        with open('clinic/users.txt', 'r') as file_handle:
            for line in file_handle:
                line = line.strip()
                content = line.split(',')
                user_list.append(content[0])
                password_list.append(content[1])
        if not self.logged_in:
            if ((username in user_list) and 
                (self.get_password_hash(password) in password_list)):
                self.logged_in = True
                return self.logged_in
            else:
                raise InvalidLoginException()
        else:
            raise DuplicateLoginException()
    
    def logout(self):
        '''
        Logs out the user by setting self.logged_in to False.
        Raises InvalidLogoutException if the user is not logged in.
        '''
        if not self.logged_in:
            raise InvalidLogoutException()
        else:
            self.logged_in = False
            return True
        
    def create_patient(self, phn: int, name: str, birth_date: str, 
                       phone: str, email: str, address: str):
        '''
        Creates and adds a new Patient object to the patient list if logged in.
        Returns the Patient object on success. Raises IllegalAccessException if not logged in.
        '''
        if self.logged_in:
            return self.patient_dao.create_patient(phn, name, birth_date, phone, email, address)
        else:
            raise IllegalAccessException()

    def search_patient(self, phn: int):
        '''
        Searches for a patient by PHN if logged in.
        Returns the Patient object if found, otherwise None. Raises IllegalAccessException if not logged in.
        '''
        if self.logged_in:
            return self.patient_dao.search_patient(phn)
        else:
            raise IllegalAccessException()
        
    def retrieve_patients(self, key: str):
        '''
        Retrieves a list of Patient objects with names matching the given key if logged in.
        Raises IllegalAccessException if not logged in.
        '''
        if self.logged_in:
            return self.patient_dao.retrieve_patients(key)
        else:
            raise IllegalAccessException()
    
    def update_patient(self, old_phn: int, phn: int, name: str, 
                       birth_date: str, phone: str, email: str, address: str):
        '''
        Updates patient information for a given old PHN if logged in.
        Raises IllegalOperationException if the patient being updated is the current patient or if there is a PHN conflict.
        Raises IllegalAccessException if not logged in.
        '''
        if self.logged_in:
            if self.search_patient(old_phn) == self.current_patient:
                raise IllegalOperationException()
            else:
                patient_obj = Patient(phn, name, birth_date, phone, email, address)
                return self.patient_dao.update_patient(old_phn, patient_obj)
        else:
            raise IllegalAccessException()
    
    def delete_patient(self, phn: int):
        '''
        Deletes a Patient object identified by PHN if logged in.
        Raises IllegalOperationException if the patient is the current patient.
        Raises IllegalAccessException if not logged in.
        '''
        if self.logged_in:
            if self.search_patient(phn) == self.current_patient:
                raise IllegalOperationException()
            else:
                return self.patient_dao.delete_patient(phn)
        else:
            raise IllegalAccessException()
    
    def list_patients(self):
        '''
        Returns a list of all Patient objects if logged in.
        Raises IllegalAccessException if not logged in.
        '''
        if self.logged_in:
            return self.patient_dao.list_patients()
        else:
            raise IllegalAccessException()
        
    def get_current_patient(self):
        '''
        Returns the current patient if one is set and the user is logged in.
        Raises IllegalAccessException if not logged in.
        '''
        if self.logged_in:
            if self.current_patient is None:
                return None
            else:
                return self.current_patient
        else:
            raise IllegalAccessException()
    
    def set_current_patient(self, phn: int):
        '''
        Sets the current patient using the given PHN if logged in.
        Raises IllegalOperationException if the PHN is not found in the patient list.
        Raises IllegalAccessException if not logged in.
        '''
        if self.logged_in:
            patient_list = self.patient_dao.patient_list
            phn_list = [patient.phn for patient in patient_list]
            if phn in phn_list:
                self.current_patient = self.search_patient(phn)
                return True
            else:
                raise IllegalOperationException()
        else:
            raise IllegalAccessException()
    
    def unset_current_patient(self):
        '''
        Clears the current patient by setting it to None if logged in.
        Raises IllegalAccessException if not logged in.
        '''
        if self.logged_in:
            self.current_patient = None
        else:
            raise IllegalAccessException()

    def create_note(self, text: str):
        '''
        Creates a new Note object for the current patient if logged in.
        Raises NoCurrentPatientException if there is no current patient.
        Raises IllegalAccessException if not logged in.
        '''
        if self.logged_in:
            current_patient = self.get_current_patient()
            if current_patient is not None:
                current_record = current_patient.patient_record
                new_note = current_record.create_note(text)
                return new_note
            else:
                raise NoCurrentPatientException()
        else:
            raise IllegalAccessException()
    
    def search_note(self, num: int):
        '''
        Searches for a Note object in the current patient's record using a note number if logged in.
        Returns the Note object if found. Raises NoCurrentPatientException if there is no current patient.
        Raises IllegalAccessException if not logged in.
        '''
        if self.logged_in:
            current_patient = self.get_current_patient()
            if current_patient is None:
                raise NoCurrentPatientException()
            else:
                current_record = current_patient.patient_record
                obtained_note = current_record.search_note(num)
                return obtained_note
        else:
            raise IllegalAccessException()

    def retrieve_notes(self, txt: str):
        '''
        Retrieves all Note objects containing the given text for the current patient if logged in.
        Raises NoCurrentPatientException if there is no current patient.
        Raises IllegalAccessException if not logged in.
        '''
        if self.logged_in:
            current_patient = self.get_current_patient()
            if current_patient is None:
                raise NoCurrentPatientException()
            else:
                current_record = current_patient.patient_record
                retrieved_notes = current_record.retrieve_notes(txt)
                return retrieved_notes
        else:
            raise IllegalAccessException()

    def update_note(self, code: int, text: str):
        '''
        Updates the text and date of a Note object identified by code in the current patient's record if logged in.
        Raises NoCurrentPatientException if there is no current patient.
        Raises IllegalAccessException if not logged in.
        '''
        if self.logged_in:
            current_patient = self.get_current_patient()
            if current_patient is None:
                raise NoCurrentPatientException()
            else:
                current_record = current_patient.patient_record
                return current_record.update_note(code, text)       
        else:
            raise IllegalAccessException()

    def delete_note(self, code: int):
        '''
        Deletes a Note object identified by code from the current patient's record if logged in.
        Raises NoCurrentPatientException if there is no current patient.
        Raises IllegalAccessException if not logged in.
        '''
        if self.logged_in:
            current_patient = self.get_current_patient()
            if current_patient is None:
                raise NoCurrentPatientException()
            else:
                current_record = current_patient.patient_record
                retrieved_notes = current_record.delete_note(code)
                return retrieved_notes        
        else:
            raise IllegalAccessException()
    
    def list_notes(self):
        '''
        Returns all Note objects from the current patient's record in reverse order if logged in.
        Raises NoCurrentPatientException if there is no current patient.
        Raises IllegalAccessException if not logged in.
        '''
        if self.logged_in:
            current_patient = self.get_current_patient()
            if current_patient is None:
                raise NoCurrentPatientException()
            else:
                current_record = current_patient.patient_record
                retrieved_notes = current_record.list_notes()
                return retrieved_notes
        else:
            raise IllegalAccessException()