from ....services.menu import menu_option_service
from ....utils.exceptions.menu.menu_option_exceptions import MenuOptionException
from ....data_access.schemas.menu.menu_option_schema import MenuOptionSchema

async def valid_menu_option_post(menu_option_data: MenuOptionSchema) -> MenuOptionSchema:
    exists_menu_with_same_name = await menu_option_service.exists_menu_option_by_field("name", menu_option_data.name)
    if exists_menu_with_same_name:
        raise MenuOptionException.MenuOptionAlreadyExists
    return menu_option_data

async def valid_menu_option_put(supplier_id: int, menu_option_id: int, menu_option_data: MenuOptionSchema) -> MenuOptionSchema:
    exists_menu = await menu_option_service.exists_menu_option_by_field("id", menu_option_id)
    if not exists_menu:
        raise MenuOptionException.MenuOptionNotFound

    correct_supplier = await menu_option_service.check_menu_option_supplier(supplier_id, menu_option_id)
    if not correct_supplier:
        raise MenuOptionException.MenuOptionSupplierNotFound

    return menu_option_data

async def valid_menu_option_delete(supplier_id: int, menu_option_id: int) -> MenuOptionSchema:
    exists_menu = await menu_option_service.exists_menu_option_by_field("id", menu_option_id)
    if not exists_menu:
        raise MenuOptionException.MenuOptionNotFound

    correct_supplier = await menu_option_service.check_menu_option_supplier(supplier_id, menu_option_id)
    if not correct_supplier:
        raise MenuOptionException.MenuOptionSupplierNotFound

    return menu_option_data