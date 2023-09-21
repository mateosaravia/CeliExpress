from ....utils.exceptions.app_exceptions import AppException

class RestaurantException(object):
    class RestaurantProfileAlreadyExists(AppException):
        def __init__(self):
            status_code = 409
            exception_case = "Restaurant profile already exists"
            super().__init__(self, status_code, exception_case)