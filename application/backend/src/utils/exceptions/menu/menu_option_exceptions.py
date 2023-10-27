from .... utils.exceptions.app_exceptions import AppException

class MenuOptionException(object):
    class MenuOptionAlreadyExists(AppException):
        def __init__(self):
            status_code = 409
            exception_case = "Menu option already exists"
            super().__init__(status_code, exception_case)

    class MenuOptionNotFound(AppException):
        def __init__(self):
            status_code = 404
            exception_case = "Menu option not found"
            super().__init__(status_code, exception_case)

    class MenuOptionSupplierNotFound(AppException):
        def __init__(self):
            status_code = 404
            exception_case = "Menu option supplier not found"
            super().__init__(status_code, exception_case)