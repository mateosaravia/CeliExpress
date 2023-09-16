from ....config.database import get_db

from ...models.users.user_model import UserModel
from ...schemas.users.user_schema import UserSchema

db = get_db()

async def add_user_to_db(user_item: UserSchema) -> UserModel:
    user = UserModel(**user.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

async def get_user_by_email(email: str) -> UserModel:
    user = db.query(UserModel).filter(UserModel.email == email).first()
    return user