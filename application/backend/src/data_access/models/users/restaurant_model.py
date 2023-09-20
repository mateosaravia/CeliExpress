from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from ....config.database import Base
from .user_model import UserModel

class RestaurantModel(Base):
    __tablename__ = "Restaurant_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(UserModel.id))
    address = Column(String(128))
    authorized = Column(Boolean)
    phone = Column(String(20))