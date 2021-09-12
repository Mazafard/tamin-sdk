from enum import IntEnum


class Prescription:
    """
    Create a Prescription object from the JSON data
    retrieved from the API
    """

    def __init__(self, prescription_data):
        for k in iter(prescription_data):
            setattr(self, k, prescription_data[k])


class DocType(object):

    def __init__(self, doc_type):
        self.doc_type = doc_type


class DocEprsc(DocType):

    def __init__(self):
        self.DOCTOR = '1'
        self.doc_type = super().__init__(doc_type=self.DOCTOR)


class PrescriptionType(IntEnum):
    """
    Type for Prescription
    """
    DRUG = 1
    PARACLINIC = 2
    VISIT = 3
    VISIT_SERVICE = 4
    SERVICE = 5
