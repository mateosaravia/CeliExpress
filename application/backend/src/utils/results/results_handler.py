from ..exceptions.app_exceptions import AppExceptionCase

class ServiceResult(object):
    def __init__(self, arg):
        if isinstance(arg, AppExceptionCase):
            self.success = False
            self.exception_case = arg.exception_case
            self.status_code = arg.status_code
        else:
            self.success = True
            self.exception_case = None
            self.status_code = None
        self.value = arg

    def __str__(self):
        if self.success:
            return "[Success]"
        return f'[Exception] "{self.exception_case}"'

    def __enter__(self):
        return self.value

    def __exit__(self, *kwargs):
        pass

def handle_result(result: ServiceResult):
    if not result.success:
        with result as exception:
            raise exception
    with result as result:
        return result