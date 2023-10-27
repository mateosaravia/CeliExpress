from ....services.menu import product_service
from ....utils.exceptions.menu.product_exceptions import ProductException
from ....data_access.schemas.menu.product_schema import ProductSchema

async def valid_product_post(product_data: ProductSchema) -> ProductSchema:
    exists_product_with_same_name = await product_service.exists_product_by_field("name", product_data.name)
    if exists_product_with_same_name:
        raise ProductException.ProductAlreadyExists
    return product_data

async def valid_product_put(product_id: int, product_data: ProductSchema) -> ProductSchema:
    exists_product = await product_service.exists_product_by_field("id", product_id)
    if not exists_product:
        raise ProductException.ProductNotFound
    return product_data

async def valid_product_delete(product_id: int) -> ProductSchema: 
    exists_product = await product_service.exists_product_by_field("id", product_id)
    if not exists_product:
        raise ProductException.ProductNotFound
    return product_data