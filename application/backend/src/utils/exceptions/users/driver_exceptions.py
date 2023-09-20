from ....utils.exceptions.app_exceptions import AppException

class DriverException(object):
    class DriverProfileAlreadyExists(AppException):
        def __init__(self):
            status_code = 409
            exception_case = "Driver profile already exists"
            super().__init__(self, status_code, exception_case)

    class DriverProfileNotFound(AppException):
        def __init__(self):
            status_code = 404
            exception_case = "Driver profile not found"
            super().__init__(self, status_code, exception_case)