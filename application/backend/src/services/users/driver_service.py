from ...data_access.schemas.users.driver_schema import DriverSchema
from ...data_access.repositories.users import driver_repository
from ...utils.results.results_handler import ServiceResult
from ...utils.exceptions.users.driver_exceptions import DriverException

async def create_driver_profile(driver_data, user_id):
    exists = get_profile_by_user(user_id)
    if exists:
        return ServiceResult(DriverException.DriverProfileAlreadyExists())

    new_profile = DriverSchema(**driver_data)
    added_profile = driver_repository.add_driver_profile(new_profile, user_id)

    return ServiceResult(added_profile)