from ....config.database import get_db

from ...models.users.supplier_model import SupplierModel
from ...schemas.users.supplier_schema import SupplierSchema

db = get_db()

async def add_supplier_profile(supplier_data: supplierSchema, user_id: int) -> supplierModel:
    supplier = supplierModel(**supplier_data.dict(), user_id=user_id)
    db.add(supplier)
    db.commit()
    db.refresh(supplier)
    return supplier

async def get_supplier_profile_by_user(user_id: int) -> supplierModel:
    supplier = db.query(supplierModel).filter(supplierModel.user_id == user_id).first()
    return supplier