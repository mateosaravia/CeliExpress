from pydantic import Field, BaseModel

class SupplierSchema(BaseModel):
    address: str = Field(default=None, min_length=0)
    authorized: bool = Field(default=False)
    phone: str = Field(default=None, min_length=0, max_length=15)