from .... utils.exceptions.app_exceptions import AppException

class ProductException(object):
    class ProductAlreadyExists(AppException):
        def __init__(self):
            status_code = 409
            exception_case = "Product already exists"
            super().__init__(status_code, exception_case)

    class ProductNotFound(AppException):
        def __init__(self):
            status_code = 404
            exception_case = "Product not found"
            super().__init__(status_code, exception_case)