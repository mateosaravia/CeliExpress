from ....utils.exceptions.app_exceptions import AppException

class TokenException(object):
    class InvalidToken(AppException):
        def __init__(self):
            status_code = 401
            exception_case = "Token is invalid"
            super().__init__(status_code, exception_case)

    class TokenExpired(AppException):
        def __init__(self):
            status_code = 401
            exception_case = "Token has expired"
            super().__init__(status_code, exception_case)