from ...schemas.users.driver_schema import DriverSchema

def add_driver(driver):
    new_driver = DriverSchema(**driver)
    return new_driver