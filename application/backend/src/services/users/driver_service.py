from ...data_access.schemas.users.driver_schema import DriverSchema
from ...data_access.repositories.users import driver_repository
from ...utils.results.result_handler import Result
from ...utils.exceptions.users.driver_exceptions import DriverException

async def create_driver_profile(driver_data):
    user_id = driver_data.user_id
    exists = await driver_repository.get_driver_profile(user_id)
    if exists:
        return Result(DriverException.DriverProfileAlreadyExists)

    added_profile = await driver_repository.add_driver_profile(driver_data)

    return ServiceResult(added_profile)