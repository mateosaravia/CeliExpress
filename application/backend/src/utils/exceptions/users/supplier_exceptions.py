from ....utils.exceptions.app_exceptions import AppException

class SupplierException(object):
    class SupplierProfileAlreadyExists(AppException):
        def __init__(self):
            status_code = 409
            exception_case = "Supplier profile already exists"
            super().__init__(self, status_code, exception_case)

    class SupplierProfileNotFound(AppException):
        def __init__(self):
            status_code = 404
            exception_case = "Supplier profile not found"
            super().__init__(self, status_code, exception_case)