from ...data_access.schemas.users.user_schema import UserSchema
from ...data_access.repositories.users import user_repository
from ...utils.results.results_handler import ServiceResult
from ...utils.exceptions.users.user_exceptions import UserException

async def create_user(user_data):
    print(user_data)
    exists = await user_repository.get_user_by_email(user_data.email)
    if exists:
        return ServiceResult(UserException.UserAlreadyExists())

    added_user = await user_repository.add_user(user_data)

    return ServiceResult(added_user)