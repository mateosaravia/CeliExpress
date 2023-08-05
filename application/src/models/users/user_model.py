from pydantic import BaseModel

def get_current_datetime():
    return datetime.now()

class UserSchema(BaseModel):
    name: str
    email: str
    password: str
    age: int = Field(ge=12)
    created_at: datetime = Field(default_factory=get_current_datetime)