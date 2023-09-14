from utils.exceptions.app_exception import AppExceptionCase

class AppException(object):

    def user_not_found():
        status_code = 404
        exception_case = "User not found"
        return AppExceptionCase(status_code, exception_case)

    def user_already_exists():
        status_code = 409
        exception_case = "User already exists"
        return AppExceptionCase(status_code, exception_case)