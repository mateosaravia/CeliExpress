from pydantic import BaseModel, Field, EmailStr, validator
from ....utils.constants.user import UserRoles
from datetime import datetime
import re

class UserSchema(BaseModel):
    username: str = Field(min_length=4, max_length=50)
    email: str = Field(default=None, min_length=1)
    password: str = Field(default=None, min_length=8, max_length=50)
    registration_date: datetime = Field(default_factory=datetime.now)
    role: str = Field(default=UserRoles.USER.value, validate=lambda x: x in UserRoles.__dict__.values())

    @validator("email")
    def check_email_format(cls, v):
        regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b$'
        if not re.match(regex, v):
            raise ValueError('Invalid email format')