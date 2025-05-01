from ...utils.results.result_handler import Result

from ...data_access.schemas.menu.menu_option_schema import MenuOptionSchema
from ...data_access.repositories.menu import menu_option_repository
from ...utils.exceptions.menu.menu_option_exceptions import MenuOptionException

async def create_menu_option(menu_option: MenuOptionSchema):
    added_menu_option = await menu_option_repository.add_menu_option(menu_option)
    return Result(added_menu_option)

async def update_menu_option(menu_option_id: int, menu_option: MenuOptionSchema):
    updated_menu_option = await menu_option_repository.update_menu_option(menu_option_id, menu_option)
    return Result(updated_menu_option)

async def delete_menu_option(menu_option_id: int):
    result = await menu_option_repository.delete_menu_option(menu_option_id)
    return Result(result)

async def exists_product_by_field(field: str, value: str or int):
    exists = await menu_option_repository.exists_menu_option_by_field(field, value)
    return Result(exists)

async def check_menu_option_supplier(supplier_id: int, menu_option_id: int):
    menu_option = await menu_option_repository.get_menu_option_by_field("id", menu_option_id)
    correct_menu_option_supplier = (supplier_id == menu_option.supplier_id)

    return Result(correct_menu_option_supplier )