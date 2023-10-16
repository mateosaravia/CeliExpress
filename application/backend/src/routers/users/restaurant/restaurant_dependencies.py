from ....services.users import user_service
from ....utils.exceptions.users.user_exceptions import UserException
from ....data_access.schemas.users.restaurant_schema import RestaurantSchema
from ....utils.results.result_handler import Result

async def valid_restaurant_profile(restaurant_data: RestaurantSchema) -> RestaurantSchema:
    user = await user_service.get_user_by_field("id", restaurant_data.user_id)
    if user.value == None:
        raise UserException.UserNotFound

    return restaurant_data