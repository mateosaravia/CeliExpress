from fastapi import APIRouter
from ...utils.results.results_handler import handle_result

from ...data_access.schemas.users.driver_schema import DriverSchema
from ...services.users import driver_service

router = APIRouter()

@router.post("/driver-profile/{user_id}", response_model=DriverSchema)
async def post_driver_profile(driver_data: DriverSchema, user_id: int):
    driver = await driver_service.create_driver(driver_data, user_id)
    return handle_result(driver)