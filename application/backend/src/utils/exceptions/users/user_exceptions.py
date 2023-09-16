from ....utils.exceptions.app_exceptions import AppExceptionCase

class AppException(object):
    class UserNotFound(AppExceptionCase):
        def __init__(self):
            status_code = 404
            exception_case = "User not found"
            AppExceptionCase.__init__(self, status_code, exception_case)


    class UserAlreadyExists(AppExceptionCase):
        def __init__(self):
            status_code = 409
            exception_case = "User already exists"
            AppExceptionCase.__init__(self, status_code, exception_case)