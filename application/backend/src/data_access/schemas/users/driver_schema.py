from pydantic import Field, BaseModel

class DriverSchema(BaseModel):
    user_id: int = Field(default=None)
    authorized: bool = Field(default=False)
    license_plate: str = Field(default=None, min_length=0)
    phone: str = Field(default=None, min_length=0, max_length=15)