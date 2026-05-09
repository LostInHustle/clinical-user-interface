"""Controller module for the clinical user interface."""
import hashlib
from typing import Optional, List

from clinic.patient_record import PatientRecord
from clinic.patient import Patient
from clinic.dao.patient_dao_json import PatientDAOJSON
from clinic.exception.invalid_login_exception import InvalidLoginException
from clinic.exception.duplicate_login_exception import DuplicateLoginException
from clinic.exception.invalid_logout_exception import InvalidLogoutException
from clinic.exception.illegal_access_exception import IllegalAccessException
from clinic.exception.illegal_operation_exception import IllegalOperationException
from clinic.exception.no_current_patient_exception import NoCurrentPatientException


class Controller:
    """Main controller for managing patient records and user authentication."""
    
    USERS_FILE = 'clinic/users.txt'
    
    def __init__(self, autosave: bool = False):
        """
        Initializes a Controller object.
        
        Args:
            autosave: If True, automatically saves data after any modification.
        """
        self.logged_in = False
        self.autosave = autosave
        self.patient_dao = PatientDAOJSON(autosave)
        self.current_patient: Optional[Patient] = None
    
    def _check_logged_in(self) -> None:
        """Raises IllegalAccessException if user is not logged in."""
        if not self.logged_in:
            raise IllegalAccessException()
    
    def _check_current_patient(self) -> Patient:
        """Returns current patient or raises NoCurrentPatientException."""
        patient = self.get_current_patient()
        if patient is None:
            raise NoCurrentPatientException()
        return patient
    
    def get_password_hash(self, password: str) -> str:
        """
        Returns the SHA-256 hash of the given password string.
        
        Args:
            password: The password to hash.
        Returns:
            The hexadecimal digest of the SHA-256 hash.
        """
        return hashlib.sha256(password.encode('utf-8')).hexdigest()
    
    def _load_credentials(self) -> tuple[List[str], List[str]]:
        """Load user credentials from file.
        
        Returns:
            Tuple of (usernames, password_hashes) lists.
        """
        user_list = []
        password_list = []
        with open(self.USERS_FILE, 'r') as file_handle:
            for line in file_handle:
                line = line.strip()
                content = line.split(',')
                user_list.append(content[0])
                password_list.append(content[1])
        return user_list, password_list

    def login(self, username: str, password: str) -> bool:
        """
        Authenticates the user with the given username and password.
        
        Args:
            username: The user's login name.
            password: The user's password.
        Returns:
            True if login successful.
        Raises:
            InvalidLoginException: If credentials are incorrect.
            DuplicateLoginException: If already logged in.
        """
        if self.logged_in:
            raise DuplicateLoginException()
        
        user_list, password_list = self._load_credentials()
        if (username in user_list and 
            self.get_password_hash(password) in password_list):
            self.logged_in = True
            return True
        else:
            raise InvalidLoginException()
    
    def logout(self) -> bool:
        """
        Logs out the user.
        
        Returns:
            True if logout successful.
        Raises:
            InvalidLogoutException: If the user is not logged in.
        """
        if not self.logged_in:
            raise InvalidLogoutException()
        self.logged_in = False
        return True
        
    def create_patient(self, phn: int, name: str, birth_date: str, 
                       phone: str, email: str, address: str) -> Patient:
        """
        Creates and adds a new Patient object to the patient list.
        
        Raises:
            IllegalAccessException: If not logged in.
        """
        self._check_logged_in()
        return self.patient_dao.create_patient(phn, name, birth_date, phone, email, address)

    def search_patient(self, phn: int) -> Optional[Patient]:
        """
        Searches for a patient by PHN.
        
        Raises:
            IllegalAccessException: If not logged in.
        """
        self._check_logged_in()
        return self.patient_dao.search_patient(phn)
        
    def retrieve_patients(self, key: str) -> List[Patient]:
        """
        Retrieves a list of Patient objects with names matching the given key.
        
        Raises:
            IllegalAccessException: If not logged in.
        """
        self._check_logged_in()
        return self.patient_dao.retrieve_patients(key)
    
    def update_patient(self, old_phn: int, phn: int, name: str, 
                       birth_date: str, phone: str, email: str, address: str) -> bool:
        """
        Updates patient information for a given old PHN.
        
        Raises:
            IllegalOperationException: If the patient being updated is the current patient 
                                       or if there is a PHN conflict.
            IllegalAccessException: If not logged in.
        """
        self._check_logged_in()
        patient_to_update = self.search_patient(old_phn)
        if patient_to_update == self.current_patient:
            raise IllegalOperationException()
        patient_obj = Patient(phn, name, birth_date, phone, email, address)
        return self.patient_dao.update_patient(old_phn, patient_obj)
    
    def delete_patient(self, phn: int) -> bool:
        """
        Deletes a Patient object identified by PHN.
        
        Raises:
            IllegalOperationException: If the patient is the current patient.
            IllegalAccessException: If not logged in.
        """
        self._check_logged_in()
        if self.search_patient(phn) == self.current_patient:
            raise IllegalOperationException()
        return self.patient_dao.delete_patient(phn)
    
    def list_patients(self) -> List[Patient]:
        """
        Returns a list of all Patient objects.
        
        Raises:
            IllegalAccessException: If not logged in.
        """
        self._check_logged_in()
        return self.patient_dao.list_patients()
        
    def get_current_patient(self) -> Optional[Patient]:
        """
        Returns the current patient if one is set.
        
        Raises:
            IllegalAccessException: If not logged in.
        """
        self._check_logged_in()
        return self.current_patient
    
    def set_current_patient(self, phn: int) -> bool:
        """
        Sets the current patient using the given PHN.
        
        Raises:
            IllegalOperationException: If the PHN is not found in the patient list.
            IllegalAccessException: If not logged in.
        """
        self._check_logged_in()
        patient_list = self.patient_dao.patient_list
        phn_list = [patient.phn for patient in patient_list]
        if phn in phn_list:
            self.current_patient = self.search_patient(phn)
            return True
        else:
            raise IllegalOperationException()
    
    def unset_current_patient(self) -> None:
        """
        Clears the current patient by setting it to None.
        
        Raises:
            IllegalAccessException: If not logged in.
        """
        self._check_logged_in()
        self.current_patient = None

    def create_note(self, text: str) -> 'Note':
        """
        Creates a new Note object for the current patient.
        
        Raises:
            NoCurrentPatientException: If there is no current patient.
            IllegalAccessException: If not logged in.
        """
        self._check_logged_in()
        current_patient = self._check_current_patient()
        current_record = current_patient.patient_record
        return current_record.create_note(text)
    
    def search_note(self, num: int) -> 'Note':
        """
        Searches for a Note object in the current patient's record using a note number.
        
        Raises:
            NoCurrentPatientException: If there is no current patient.
            IllegalAccessException: If not logged in.
        """
        self._check_logged_in()
        current_patient = self._check_current_patient()
        current_record = current_patient.patient_record
        return current_record.search_note(num)

    def retrieve_notes(self, txt: str) -> List['Note']:
        """
        Retrieves all Note objects containing the given text for the current patient.
        
        Raises:
            NoCurrentPatientException: If there is no current patient.
            IllegalAccessException: If not logged in.
        """
        self._check_logged_in()
        current_patient = self._check_current_patient()
        current_record = current_patient.patient_record
        return current_record.retrieve_notes(txt)

    def update_note(self, code: int, text: str) -> bool:
        """
        Updates the text and date of a Note object identified by code.
        
        Raises:
            NoCurrentPatientException: If there is no current patient.
            IllegalAccessException: If not logged in.
        """
        self._check_logged_in()
        current_patient = self._check_current_patient()
        current_record = current_patient.patient_record
        return current_record.update_note(code, text)       

    def delete_note(self, code: int) -> bool:
        """
        Deletes a Note object identified by code from the current patient's record.
        
        Raises:
            NoCurrentPatientException: If there is no current patient.
            IllegalAccessException: If not logged in.
        """
        self._check_logged_in()
        current_patient = self._check_current_patient()
        current_record = current_patient.patient_record
        return current_record.delete_note(code)        
    
    def list_notes(self) -> List['Note']:
        """
        Returns all Note objects from the current patient's record in reverse order.
        
        Raises:
            NoCurrentPatientException: If there is no current patient.
            IllegalAccessException: If not logged in.
        """
        self._check_logged_in()
        current_patient = self._check_current_patient()
        current_record = current_patient.patient_record
        return current_record.list_notes()