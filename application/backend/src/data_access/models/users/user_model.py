from sqlalchemy import Boolean, Column, Integer, String, DateTime
from ....config.database import Base

class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    registration_date = Column(DateTime)
    role = Column(String)
