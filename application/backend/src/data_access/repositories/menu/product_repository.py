from ....config.database import get_db

from ...models.menu.product_model import ProductModel
from ...schemas.menu.product_schema import ProductSchema

db = get_db()

async def add_product(product: ProductSchema) -> ProductModel:
    product = ProductModel(**product.dict())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

async def delete_product(product_id: int) -> ProductModel:
    product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    db.delete(product)
    db.commit()
    return product

async def udpate_product(product_id: int, new_product_data: ProductSchema) -> ProductModel:
    product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    for field, value in new_product_data:
        setattr(product, field, value)
    db.commit()
    db.refresh(product)
    return product

async def exists_product_by_field(field: str, value) -> ProductModel:
    attribute = getattr(ProductModel, field)
    exists = db.query(ProductModel).filter(attribute == value).first() is not None
    return exists