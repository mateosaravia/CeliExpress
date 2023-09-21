from pydantic import Field, BaseModel

class DriverSchema(BaseModel):
    user_id: int = Field(default=None)
    license_plate: str = Field(default=None, min_length=0)
    phone: str = Field(default=None, min_length=0, max_length=15)
    authorized: bool = False