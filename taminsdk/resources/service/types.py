from enum import IntEnum


class Service:
    """
    Create a Prescription object from the JSON data
    retrieved from the API
    """

    def __init__(self, services_data):
        for k in iter(services_data):
            setattr(self, k, services_data[k])

