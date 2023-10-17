from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from ....config.database import Base
from .user_model import UserModel

class SupplierModel(Base):
    __tablename__ = "Supplier_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(UserModel.id))
    address = Column(String(128), nullable=False)
    authorized = Column(Boolean, nullable=False)
    phone = Column(String(20), nullable=False)