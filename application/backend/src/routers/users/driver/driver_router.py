from fastapi import APIRouter, Depends
from ....utils.results.result_handler import handle_result

from ....data_access.schemas.users.driver_schema import DriverSchema
from ....services.users import driver_service
from .driver_dependencies import valid_driver_profile

router = APIRouter()

@router.post("/driver/profile", response_model=DriverSchema)
async def post_driver_profile(driver_data: DriverSchema = Depends(valid_driver_profile)):
    driver = await driver_service.create_driver_profile(driver_data)
    return handle_result(driver)