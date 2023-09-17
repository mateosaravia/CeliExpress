from ...data_access.schemas.users.user_schema import UserSchema
from ...data_access.repositories.users import user_repository
from ...utils.results.results_handler import ServiceResult
from ...utils.exceptions.users.user_exceptions import UserException

async def create_user(user_data):
    exists = get_user_by_email(user_data.email)
    if exists:
        return ServiceResult(UserException.UserAlreadyExists())

    new_user = UserSchema(**user_data)
    added_user = user_repository.add_user(new_user)

    return ServiceResult(added_user)

async def get_user_by_email(email):
    user = user_repository.get_user_by_email(email)
    return ServiceResult(user)