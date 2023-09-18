from ....utils.exceptions.app_exceptions import AppExceptionCase

class SupplierException(Exception):
    class SupplierProfileAlreadyExists(AppExceptionCase):
        def __init__(self):
            status_code = 409
            exception_case = "Supplier profile already exists"
            AppExceptionCase.__init__(self, status_code, exception_case)


    class SupplierProfileNotFound(AppExceptionCase):
        def __init__(self):
            status_code = 404
            exception_case = "Supplier profile not found"
            AppExceptionCase.__init__(self, status_code, exception_case)