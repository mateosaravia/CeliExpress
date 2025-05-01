from pydantic import Field, BaseModel, validator
from ....utils.constants.menu_constants import MenuOptionCategories

class MenuOptionSchema(BaseModel):
    name: str = Field(default=None, min_length=1, max_length=50)
    description: str = Field(default=None, min_length=10, max_length=200)
    price: float = Field(default=None, gt=0)
    available: bool = False
    category: str 

    @validator('category')
    def validate_category(cls, v):
        if v not in [category.value for category in MenuOptionCategories]:
            raise ValueError("Invalid menu category")
        return v