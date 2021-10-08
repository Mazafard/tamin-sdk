class Service:
    """
    Create a Prescription object from the JSON data
    retrieved from the API
    """

    def __init__(self, services_data):
        for k in iter(services_data):
            setattr(self, k, services_data[k])

    def __iter__(self):
        ''' Returns the Iterator object '''
        return ServiceIterator(self)


class ServiceIterator:
    ''' Iterator class '''

    def __init__(self, service):
        # Service object reference
        self._service = service
        # member variable to keep track of current index
        self._index = 0

    def __next__(self):
        ''''Returns the next value from service object's lists '''
        if self._index < (len(self._service)):
            result = self._service[self._index]
            self._index += 1
            return result
            # End of Iteration
        raise StopIteration
