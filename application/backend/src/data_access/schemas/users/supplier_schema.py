from pydantic import Field, BaseModel

class SupplierSchema(BaseModel):
    user_id: int = Field(default=None)
    address: str = Field(default=None, min_length=0)
    _authorized: bool = False
    phone: str = Field(default=None, min_length=0, max_length=15)