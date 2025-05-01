from sqlalchemy import Column, Integer, ForeignKey, Table
from ....config.database import Base

menu_product_association = Table('menu_product_association', Base.metadata,
    Column('menu_option_id', Integer, ForeignKey('MenuOptionModel.id')),
    Column('product_id', Integer, ForeignKey('ProductModel.id'))
)