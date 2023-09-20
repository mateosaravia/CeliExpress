from pydantic import Field, BaseModel

class RestaurantSchema(BaseModel):
    user_id: int = Field(default=None)
    address: str = Field(default=None, min_length=0)
    authorized: bool = Field(default=False)
    phone: str = Field(default=None, min_length=0, max_length=15)