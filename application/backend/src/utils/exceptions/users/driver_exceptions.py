from ....utils.exceptions.app_exceptions import AppException

class DriverException(object):
    class DriverProfileAlreadyExists(AppException):
        def __init__(self):
            status_code = 409
            exception_case = "A profile already exists for this user"
            super().__init__(status_code, exception_case)