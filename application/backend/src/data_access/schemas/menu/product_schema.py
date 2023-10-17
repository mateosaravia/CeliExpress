from pydantic import BaseModel, Field

from ....utils.constants.menu_option_constants import MenuProductCategories

class ProductSchema(BaseModel):
    menu_option_id: int = Field(default=None)
    name: str = Field(default=None, min_length=1, max_length=50)
    available: bool = Field(default=None)
    category: str = Field(default=None, validate=lambda x: x in MenuProductCategories.__dict__.values())