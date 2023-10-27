from fastapi import APIRouter, Depends, Header
from ...utils.results.result_handler import handle_result

from ...data_access.schemas.menu.menu_option_schema import MenuOptionSchema
from ...services.menu import menu_option_service
from .menu_option_dependencies import valid_menu_option_post, valid_menu_option_put, valid_menu_option_delete

router = APIRouter()

@router.post("/suppliers/{supplier_id}/menu-options", response_model=MenuOptionSchema)
async def post_menu_option(supplier_id: int, menu_option_data: MenuOptionSchema = Depends(valid_menu_option_post)):
    post_result = await menu_option_service.create_menu_option(supplier_id, menu_option_data)
    return 
