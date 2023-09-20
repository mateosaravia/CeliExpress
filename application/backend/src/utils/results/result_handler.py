from ..exceptions.app_exceptions import AppException

class Result(object):
    def __init__(self, arg):
        if isinstance(arg, AppException):
            self.success = False
            self.exception_case = arg.exception_case
            self.status_code = arg.status_code
        else:
            self.success = True
            self.exception_case = None
            self.status_code = None
        self.value = arg

    def __enter__(self):
        return self.value

    def __exit__(self, *kwargs):
        pass

def handle_result(result: Result):
    if not result.success:
        with result as exception:
            raise exception
    with result as result:
        return result