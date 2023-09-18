from ....utils.exceptions.app_exceptions import AppExceptionCase

class RestaurantException(Exception):
    class RestaurantProfileAlreadyExists(AppExceptionCase):
        def __init__(self):
            status_code = 409
            exception_case = "Restaurant profile already exists"
            AppExceptionCase.__init__(self, status_code, exception_case)


    class RestaurantProfileNotFound(AppExceptionCase):
        def __init__(self):
            status_code = 404
            exception_case = "Restaurant profile not found"
            AppExceptionCase.__init__(self, status_code, exception_case)