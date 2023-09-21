from ...data_access.schemas.users.restaurant_schema import RestaurantSchema
from ...data_access.repositories.users import restaurant_repository
from ...utils.results.result_handler import Result
from ...utils.exceptions.users.restaurant_exceptions import RestaurantException

async def create_restaurant_profile(restaurant_data):
    user_id = restaurant_data.user_id
    exists = await restaurant_repository.get_restaurant_profile(user_id)
    if exists:
        return Result(RestaurantException.RestaurantProfileAlreadyExists)

    added_profile = await restaurant_repository.add_restaurant_profile(restaurant_data)

    return Result(added_profile)
