from ....utils.exceptions.app_exceptions import AppException

class SessionException(object):
    class InvalidCredentials(AppException):
        def __init__(self):
            status_code = 401
            exception_case = "Invalid credentials"
            super().__init__(status_code, exception_case)
