from pydantic import BaseModel, Field, EmailStr
from ....utils.constants.user_roles import UserRoles
from datetime import datetime

class UserSchema(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: str = Field(default=None, min_length=0)
    password: str = Field(default=None, min_length=0)
    registration_date: datetime = Field(default_factory=datetime.now)
    role: str = Field(default=UserRoles.USER.value, validate=lambda x: x in UserRoles.__dict__.values())