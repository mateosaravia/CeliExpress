from pydantic import Field, BaseModel
from ....utils.constants.menu_constants import MenuOptionCategories

class MenuOptionSchema(BaseModel):
    name: str = Field(default=None, min_length=1, max_length=50)
    description: str = Field(default=None, min_length=10, max_length=200)
    price: float = Field(default=None, gt=0)
    available: bool = False
    category: str = Field(default=MenuOptionCategories.OTHER.value, validate=lambda x: x in MenuOptionCategories.__dict__.values())