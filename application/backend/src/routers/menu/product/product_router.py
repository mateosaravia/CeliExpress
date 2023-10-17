from fastapi import APIRouter, Depends, Header
from ...utils.results.result_handler import handle_result

from ...data_access.schemas.menu.product_schema import ProductSchema
from ...services.menu import product_service
from .product_dependencies import valid_product_post, valid_product_put, valid_product_delete

@router.post("/products", response_model=ProductSchema)
async def post_product(product_data: ProductSchema = Depends(valid_product_post)):
    post_result = await product_service.create_product(product_data)
    handle_result(post_result)

@router.put("/products", response_model=ProductSchema)
async def put_product(product_data: ProductSchema = Depends(valid_product_put)):
    update_result = await product_service.update_product(product_data)
    handle_result(update_result)

@router.delete("/products")
async def delete_product(product_data: ProductSchema = Depends(valid_product_delete)):
    delete_result = await product_service.delete_product(product_data)
    handle_result(delete_result)