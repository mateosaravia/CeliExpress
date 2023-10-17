from ..app_exceptions import AppException

class UserException(object):
    class UserNotFound(AppException):
        def __init__(self):
            status_code = 404
            exception_case = "User not found"
            super().__init__(status_code, exception_case)

    class UserAlreadyExists(AppException):
        def __init__(self):
            status_code = 409
            exception_case = "User already exists"
            super().__init__(status_code, exception_case)

    class UsernameAlreadyExists(AppException):
        def __init__(self):
            status_code = 409
            exception_case = "This username has already been used"
            super().__init__(status_code, exception_case)