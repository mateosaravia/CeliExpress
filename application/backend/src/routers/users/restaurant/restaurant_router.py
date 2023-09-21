from fastapi import APIRouter, Depends
from ....utils.results.result_handler import handle_result

from ....data_access.schemas.users.restaurant_schema import RestaurantSchema
from ....services.users import restaurant_service
from .restaurant_dependencies import valid_restaurant_profile

router = APIRouter()

@router.post("/restaurant/profile", response_model=RestaurantSchema)
async def post_restaurant_profile(restaurant_data: RestaurantSchema = Depends(valid_restaurant_profile)):
    restaurant = await restaurant_service.create_restaurant(restaurant_data)
    return handle_result(restaurant)