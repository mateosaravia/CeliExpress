from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from ...config.database import Base
from user_model import user

class RestaurantModel(Base):
    __tablename__ = "restaurant_details"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(user.id))
    address = Column(String)
    authorized = Column(Boolean)
    phone = Column(String)