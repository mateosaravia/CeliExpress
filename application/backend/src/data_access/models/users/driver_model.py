from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from ....config.database import Base
from .user_model import UserModel

class DriverModel(Base):
    __tablename__ = "Driver_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(UserModel.id))
    license_plate = Column(String(40), nullable=False)
    authorized = Column(Boolean, nullable=False)
    phone = Column(String(20), nullable=False)