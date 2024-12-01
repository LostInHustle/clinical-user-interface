from json import JSONDecoder
from clinic.patient import Patient

class PatientDecoder(JSONDecoder):
    def __init__(self, *args, **kwargs):
        '''
        Initializes the PatientDecoder.
        Inherits from JSONDecoder and specifies the `object_hook` method to translate
        dictionaries back into Patient objects during the decoding process.
        '''
        super().__init__(object_hook=self.object_hook, *args, **kwargs)
    
    def object_hook(self, dct):
        '''
        Converts dictionaries with a specific marker ('__type__': 'Patient') 
        into Patient objects.
        - dct: The dictionary being processed.
        If the dictionary represents a Patient (indicated by '__type__'), 
        it creates and returns a Patient object using the dictionary's data.
        Otherwise, returns the dictionary as-is.
        '''
        if '__type__' in dct and dct['__type__'] == 'Patient':
            return Patient(dct['phn'], dct['name'], dct['birth_date'], 
                           dct['phone'], dct['email'], dct['address'])
        return dct