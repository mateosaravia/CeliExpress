from ....services.users import user_service
from ....utils.exceptions.users.user_exceptions import UserException
from ....data_access.schemas.users.driver_schema import DriverSchema

async def valid_driver_profile(driver_data: DriverSchema) -> DriverSchema:
    user = await user_service.get_user_by_field("id", driver_data.user_id)
    if user.value == None:
        raise UserException.UserNotFound
    return driver_data