from sqlalchemy import Boolean, Column, Integer, String, DateTime
from ....config.database import Base

class UserModel(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(40), unique=True, index=True)
    email = Column(String(64), unique=True, index=True)
    password = Column(String(128))
    registration_date = Column(DateTime)
    role = Column(String(40))
