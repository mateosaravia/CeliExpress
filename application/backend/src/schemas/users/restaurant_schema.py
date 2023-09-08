from pydantic import Field
from user_schema import UserSchema

class RestaurantSchema(UserSchema):
    phone: str = Field(default=None, min_length=0, max_length=15)
    address: str = Field(default=None, min_length=0)
    authorized: bool = Field(default=False)