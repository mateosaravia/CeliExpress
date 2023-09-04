from pydantic import BaseModel, Field, EmailStr

def get_current_datetime():
    return datetime.now()

class AdminSchema(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    email: EmailStr = Field(default=None) 
    password: str = Field(default=None)
    created_at: datetime = Field(default_factory=get_current_datetime)