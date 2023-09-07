from pydantic import Field
from user_schema import UserSchema

class DriverSchema(UserSchema):
    phone: str = Field(default=None, min_length=0, max_length=15)
    license_plate: str = Field(default=None, min_length=0)
    available: bool = Field(default=False)
    authorized: bool = Field(default=False)