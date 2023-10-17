from pydantic import Field, BaseModel

class SessionSchema(BaseModel):
    email: str = Field(default=None, min_length=0)
    password: str = Field(default=None, min_length=0)
