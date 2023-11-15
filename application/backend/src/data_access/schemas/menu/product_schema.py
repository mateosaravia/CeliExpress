from pydantic import BaseModel, Field, validator
from ....utils.constants.menu_constants import MenuProductCategories

class ProductSchema(BaseModel):
    name: str = Field(default=None, min_length=1, max_length=50)
    available: bool = Field(default=True)
    category: str

    @validator('category')
    def validate_category(cls, v):
        if v not in [category.value for category in MenuProductCategories]:
            raise ValueError("Invalid product category")
        return v
