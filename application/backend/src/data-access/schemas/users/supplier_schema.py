from pydantic import Field

class SupplierSchema(UserSchema):
    address: str = Field(default=None, min_length=0)
    authorized: bool = Field(default=False)
    phone: str = Field(default=None, min_length=0, max_length=15)