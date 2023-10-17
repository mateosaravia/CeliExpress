from ...utils.results.result_handler import Result

from ...data_access.schemas.menu.product_schema import ProductSchema
from ...data_access.repositories.menu import product_repository
from ...utils.exceptions.menu.product_exceptions import ProductException

async def create_product(product: ProductSchema):
    added_product = await product_repository.add_product(product)
    return Result(added_product)

async def update_product(product: ProductSchema, product_id: int):
    updated_product = await product_repository.update_product(product, product_id)
    return Result(updated_product)

async def delete_product(product_id: int):
    result = await product_repository.delete_product(product_id)
    return Result(result)

async def exists_product_by_field(field: str, value: str or int):
    exists = await product_repository.exists_product_by_field(field, value)
    return Result(exists)