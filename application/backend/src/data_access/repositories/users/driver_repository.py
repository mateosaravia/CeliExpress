from ....config.database import get_db

from ...models.users.driver_model import DriverModel
from ...schemas.users.driver_schema import DriverSchema

db = get_db()

async def add_driver_profile(driver_data: DriverSchema, user_id: int) -> DriverModel:
    driver = DriverModel(**driver_data.dict(), user_id=user_id)
    db.add(driver)
    db.commit()
    db.refresh(driver)
    return driver

async def get_driver_profile_by_user(user_id: int) -> DriverModel:
    driver = db.query(DriverModel).filter(DriverModel.user_id == user_id).first()
    return driver