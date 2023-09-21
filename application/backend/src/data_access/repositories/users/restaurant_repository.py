from ....config.database import get_db

from ...models.users.restaurant_model import RestaurantModel
from ...schemas.users.restaurant_schema import RestaurantSchema

db = get_db()

async def add_restaurant_profile(restaurant_data: RestaurantSchema) -> RestaurantModel:
    restaurant = RestaurantModel(**restaurant_data.dict())
    db.add(restaurant)
    db.commit()
    db.refresh(restaurant)
    return restaurant

async def get_restaurant_profile(user_id: int) -> RestaurantModel:
    restaurant = db.query(RestaurantModel).filter(RestaurantModel.user_id == user_id).first()
    return restaurant

async def exists_restaurant_profile(user_id: int) -> bool:
    exists = db.query(RestaurantModel).filter(RestaurantModel.user_id == user_id).first()
    return exists is not None