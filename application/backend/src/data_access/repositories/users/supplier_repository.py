from ....config.database import get_db

from ...models.users.supplier_model import SupplierModel
from ...schemas.users.supplier_schema import SupplierSchema

db = get_db()

async def add_supplier_profile(supplier_data: SupplierSchema, user_id: int) -> SupplierModel:
    supplier = SupplierModel(**supplier_data.dict(), user_id=user_id)
    db.add(supplier)
    db.commit()
    db.refresh(supplier)
    return supplier

async def get_supplier_profile_by_user(user_id: int) -> SupplierModel:
    supplier = db.query(SupplierModel).filter(SupplierModel.user_id == user_id).first()
    return supplier