from ...data_access.schemas.users.user_schema import UserSchema
import ...data_access.models.users.user_model as user_model

async def add_create_user(user):
    new_user = UserSchema(**user)
    added_user = user_model.add_user_to_db(new_user)
    return added_user