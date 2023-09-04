from pydantic import BaseModel, Field, EmailStr

class RestaurantSchema(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    email: EmailStr = Field(default=None, min_length=0)
    password: str = Field(default=None, min_length=0)
    phone: str = Field(default=None, min_length=0, max_length=15)
    address: str = Field(default=None, min_length=0)
    authorized: bool = Field(default=False)