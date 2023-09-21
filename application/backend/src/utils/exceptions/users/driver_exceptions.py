from ....utils.exceptions.app_exceptions import AppException

class DriverException(object):
    class DriverProfileAlreadyExists(AppException):
        def __init__(self):
            status_code = 409
            exception_case = "Driver profile already exists"
            super().__init__(self, status_code, exception_case)