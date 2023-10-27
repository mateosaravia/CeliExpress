from pydantic import BaseModel, Field
from ....utils.constants.menu_constants import MenuProductCategories

class ProductSchema(BaseModel):
    name: str = Field(default=None, min_length=1, max_length=50)
    available: bool = Field(default=True)
    category: str = Field(default=None, validate=lambda x: x in MenuProductCategories.__dict__.values())