from ...utils.results.result_handler import Result
from ...utils import hasher

from ...data_access.schemas.users.user_schema import UserSchema
from ...data_access.repositories.users import user_repository
from ...utils.exceptions.users.user_exceptions import UserException

async def create_user(user_data):
    exists = await get_user_by_field("email", user_data.email)
    if exists.value is not None:
        return Result(UserException.UserAlreadyExists())

    user_data.password = hasher.get_password_hash(user_data.password)

    added_user = await user_repository.add_user(user_data)
    return Result(added_user)

async def get_user_by_field(field, value):
    user = await user_repository.get_user_by_field(field, value)
    return Result(user)

async def exists_user_by_field(field, value):
    exists = await user_repository.exists_user_by_field(field, value)
    return Result(exists)