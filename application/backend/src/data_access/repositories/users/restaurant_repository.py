from ....config.database import get_db

from ...models.users.restaurant_model import RestaurantModel
from ...schemas.users.restaurant_schema import RestaurantSchema

db = get_db()

async def add_restaurant_profile(restaurant_data: RestaurantSchema, user_id: int) -> RestaurantModel:
    restaurant = RestaurantModel(**restaurant_data.dict(), user_id=user_id)
    db.add(restaurant)
    db.commit()
    db.refresh(restaurant)
    return restaurant

async def get_restaurant_profile_by_user(user_id: int) -> RestaurantModel:
    restaurant = db.query(RestaurantModel).filter(RestaurantModel.user_id == user_id).first()
    return restaurant