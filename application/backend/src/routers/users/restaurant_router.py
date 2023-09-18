from fastapi import APIRouter
from ...utils.results.results_handler import handle_result

from ...data_access.schemas.users.restaurant_schema import RestaurantSchema
from ...services.users import restaurant_service

router = APIRouter()

@router.post("/restaurant-profile", response_model=RestaurantSchema)
async def post_restaurant_profile(restaurant_data: RestaurantSchema, user_id: int):
    restaurant = await restaurant_service.create_restaurant(restaurant_data, user_id)
    return handle_result(restaurant)