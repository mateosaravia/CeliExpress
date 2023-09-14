class AppExceptionCase(Exception):
    def __init__(self, status_code: int, exception_case: str):
        self.exception_case = exception_case
        self.status_code = status_code