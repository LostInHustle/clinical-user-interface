import json
from clinic.patient import *
from clinic.dao.patient_dao import *
from clinic.dao.patient_encoder import PatientEncoder
from clinic.dao.patient_decoder import PatientDecoder
from clinic.exception.illegal_operation_exception import IllegalOperationException

class PatientDAOJSON(PatientDAO):
    def __init__(self, autosave: bool):
        '''
        Initializes a PatientDAOJSON instance.
        - autosave: If True, automatically saves data to the JSON file after any modification.
        Loads existing patient data from a JSON file if available, or creates a new file if not.
        '''
        self.file_name = 'clinic/patients.json'
        self.autosave = autosave
        self.patient_list = []
        if self.autosave:
            try:
                with open(self.file_name, 'r') as file_handle:
                    self.patient_list = json.load(file_handle, cls=PatientDecoder)
            except:
                # Creates a new JSON file if loading fails
                with open(self.file_name, 'w') as file_handle:
                    json.dump(self.patient_list, file_handle, cls=PatientEncoder)

    def create_patient(self, phn: int, name: str, birth_date: str, 
                       phone: str, email: str, address: str):
        '''
        Adds a new patient with the provided information if the PHN is unique.
        - phn: Patient's Personal Health Number
        - name: Patient's full name
        - birth_date: Patient's birth date
        - phone: Patient's phone number
        - email: Patient's email address
        - address: Patient's physical address
        Raises IllegalOperationException if the PHN already exists.
        Saves data automatically if autosave is enabled.
        Returns the created Patient object.
        '''
        phn_list = [person.phn for person in self.patient_list]
        if phn not in phn_list:
            new_patient = Patient(phn, name, birth_date, phone, email, address)
            self.patient_list.append(new_patient)
            if self.autosave:
                with open(self.file_name, 'w') as file_handle:
                    json.dump(self.patient_list, file_handle, cls=PatientEncoder)
            return new_patient
        else:
            raise IllegalOperationException()
    
    def search_patient(self, phn: int):
        '''
        Searches for a patient by PHN.
        - phn: The PHN of the patient to search for.
        Returns the Patient object if found, otherwise None.
        '''
        for patient in self.patient_list:
            if phn == patient.phn:
                return patient

    def retrieve_patients(self, name: str):
        '''
        Searches for patients whose names contain the given substring.
        - name: Substring to search for in patient names.
        Returns a list of matching Patient objects.
        '''
        result = []
        for patient in self.patient_list:
            if name in patient.name:
                result.append(patient)
        return result

    def update_patient(self, phn: int, patient: 'Patient'):
        '''
        Updates the information of a patient identified by PHN.
        - phn: The PHN of the patient to update.
        - patient: The new Patient object with updated information.
        Raises IllegalOperationException if the new PHN already exists in another patient.
        Saves data automatically if autosave is enabled.
        Returns True if the update is successful.
        '''
        obtained_patient = self.search_patient(phn)
        phn_list = [person.phn for person in self.patient_list]
        if obtained_patient:
            phn_list.remove(phn)
            if patient.phn in phn_list:
                raise IllegalOperationException()
            self.patient_list.remove(obtained_patient)
            self.patient_list.append(patient)
            if self.autosave:
                with open(self.file_name, 'w') as file_handle:
                    json.dump(self.patient_list, file_handle, cls=PatientEncoder)
            return True
        else:
            raise IllegalOperationException()

    def delete_patient(self, phn: int):
        '''
        Deletes the patient with the specified PHN.
        - phn: The PHN of the patient to delete.
        Raises IllegalOperationException if the patient is not found.
        Saves data automatically if autosave is enabled.
        Returns True if the deletion is successful.
        '''
        obtained_patient = self.search_patient(phn)
        if obtained_patient:
            self.patient_list.remove(obtained_patient)
            if self.autosave:
                with open(self.file_name, 'w') as file_handle:
                    json.dump(self.patient_list, file_handle, cls=PatientEncoder)
            return True
        else:
            raise IllegalOperationException()

    def list_patients(self):
        '''
        Returns the complete list of Patient objects.
        '''
        return self.patient_list