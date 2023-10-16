from enum import Enum

class UserRoles(Enum):
    USER = "user"
    ADMIN = "admin"
    SUPPLIER = "supplier"
    RESTAURANT = "restaurant"
    CUSTOMER = "customer"

class UserAttributes():
    MAX_USERNAME_LENGTH = 20
    MAX_USERNAME_LENGTH = 4
