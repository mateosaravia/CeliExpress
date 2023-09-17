from ....utils.exceptions.app_exceptions import AppExceptionCase

class DriverException(Exception):
    class DriverProfileAlreadyExists(AppExceptionCase):
        def __init__(self):
            status_code = 409
            exception_case = "Driver profile already exists"
            AppExceptionCase.__init__(self, status_code, exception_case)


    class DriverProfileNotFound(AppExceptionCase):
        def __init__(self):
            status_code = 404
            exception_case = "Driver profile not found"
            AppExceptionCase.__init__(self, status_code, exception_case)