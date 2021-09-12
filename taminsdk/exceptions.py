class AuthTokenNotSuppliedException(Exception):
    """
    Authorization token not supplied
    """
    pass


class UserLoginException(Exception):
    """
    User jobs could not be set
    """

    def __init__(self, data, status, family,reason):
        super().__init__(data)
        self.status=status
        self.family = family
        self.reason=reason
