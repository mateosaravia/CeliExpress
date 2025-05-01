from sqlalchemy import Boolean, String, Column, Integer, ForeignKey, Float
from ....config.database import Base
from ..users.supplier_model import SupplierModel

class MenuOptionModel(Base):
    __tablename__ = "Menu_options"

    id = Column(Integer, primary_key=True, index=True)
    supplier_id = Column(Integer, ForeignKey(SupplierModel.id))
    name = Column(String(50), nullable=False)
    description = Column(String(200), nullable=False)
    price = Column(Float, nullable=False)
    available = Column(Boolean, nullable=False)
    category = Column(String(20), nullable=False)
