from ....config.database import get_db

from ...models.users.user_model import UserModel
from ...schemas.users.user_schema import UserSchema

db = get_db()

async def add_user(user_data: UserSchema) -> UserModel:
    user = UserModel(**user_data.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

async def get_user_by_field(field: str, value) -> UserModel:
    attribute = getattr(UserModel, field)
    user = db.query(UserModel).filter(attribute == value).first()
    return user

async def exists_user_by_field(field: str, value) -> bool:
    attribute = getattr(UserModel, field)
    exists = db.query(UserModel).filter(attribute == value).first() is not None
    return exists

async def update_user_role(user_id: int, newRole: str) -> UserModel:
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    user.role = newRole
    db.commit()
    db.refresh(user)
    return user
