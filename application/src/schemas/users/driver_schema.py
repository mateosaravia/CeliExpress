from pydantic import BaseModel, Field, EmailStr

def get_current_datetime():
    return datetime.now()

class DriverSchema(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    email: EmailStr = Field(default=None, min_length=0)
    password: str = Field(default=None, min_length=0)
    phone: str = Field(default=None, min_length=0, max_length=15)
    license_plate: str = Field(default=None, min_length=0)
    created_at: datetime = Field(default_factory=get_current_datetime) 
    available: bool = Field(default=False)
    authorized: bool = Field(default=False)