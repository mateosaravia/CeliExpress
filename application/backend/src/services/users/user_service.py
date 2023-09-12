from ...data_access.schemas.users.user_schema import UserSchema
import ...data_access.repositories.users.user_repository as user_repository

async def create_user(user_data):
    new_user = UserSchema(**user_data)
    added_user = user_repository.add_user_to_db(new_user)
    return added_user