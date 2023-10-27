from ....config.database import get_db

from ...models.menu.menu_option_model import MenuOptionModel
from ...schemas.menu.menu_option_schema import MenuOptionSchema

db = get_db()

async def add_menu_option(menu_option: MenuOptionSchema) -> MenuOptionModel:
    menu_option = MenuOptionSchema(**menu_option.dict())
    db.add(menu_option)
    db.commit()
    db.refresh(menu_option)
    return menu_option

async def delete_menu_option(menu_option_id: int) -> MenuOptionModel:
    menu_option = db.query(MenuOptionModel).filter(MenuOptionModel.id == menu_option_id).first()
    db.delete(menu_option)
    db.commit()
    return menu_option

async def udpate_menu_option(menu_option_id: int, new_menu_option_data: MenuOptionSchema) -> MenuOptionModel:
    menu_option = db.query(MenuOptionModel).filter(MenuOptionModel.id == menu_option_id).first()
    for field, value in new_menu_option_data:
        setattr(menu_option, field, value)
    db.commit()
    db.refresh(menu_option)
    return menu_option

async def exists_menu_option_by_field(field: str, value) -> MenuOptionModel:
    attribute = getattr(MenuOptionModel, field)
    exists = db.query(MenuOptionModel).filter(attribute == value).first() is not None
    return exists

async def get_menu_option_by_field(field: str, value) -> MenuOptionModel:
    attribute = getattr(MenuOptionModel, field)
    menu_option = db.query(MenuOptionModel).filter(attribute == value).first()
    return menu_option
