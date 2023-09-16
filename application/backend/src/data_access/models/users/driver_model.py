from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from ...config.database import Base
from user_model import user

class DriverModel(Base):
    __tablename__ = "driver_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(user.id))
    license_plate = Column(String)
    authorized = Column(Boolean)
    phone = Column(String)