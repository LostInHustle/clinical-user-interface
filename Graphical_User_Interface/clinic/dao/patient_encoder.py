from json import JSONEncoder
from clinic.patient import Patient

class PatientEncoder(JSONEncoder):
    def default(self, obj):
        '''
        Converts a Patient object into a dictionary format for JSON serialization.
        - obj: The object to encode.
        
        If the object is an instance of Patient, it returns a dictionary representation,
        which includes a special key '__type__' to indicate the object type. 
        This marker helps in reconstructing the object during deserialization.
        If the object is not a Patient, it uses the default JSONEncoder behavior.
        '''
        if isinstance(obj, Patient):
            return {
                "__type__": "Patient",
                "phn": obj.phn,
                "name": obj.name,
                "birth_date": obj.birth_date,
                "phone": obj.phone,
                "email": obj.email,
                "address": obj.address
            }
        return super().default(obj)