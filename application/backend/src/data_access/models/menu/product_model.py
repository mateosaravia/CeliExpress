from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from ....config.database import Base

class ProductModel(Base):
    __tablename__ = "Products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(40), unique=True, index=True, nullable=False)
    available = Column(Boolean, nullable=False)
    category = Column(String(40), nullable=False)
