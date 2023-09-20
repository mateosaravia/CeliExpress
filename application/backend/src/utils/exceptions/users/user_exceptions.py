from ..app_exceptions import AppException

class UserException(object):
    class UserNotFound(AppException):
            def __init__(self):
                self.status_code = 404
                self.exception_case = "User not found"
                super().__init__(status_code, exception_case)

    class UserAlreadyExists(AppException):
        def __init__(self, message):
            self.status_code = 409
            self.exception_case = "User already exists"
            super().__init__(status_code, exception_case)