from fastapi import APIRouter
from ...utils.results.results_handler import handle_result

from ...data_access.schemas.users.supplier_schema import SupplierSchema
from ...services.users import supplier_service

router = APIRouter()

@router.post("/supplier-profile", response_model=SupplierSchema)
async def post_supplier_profile(supplier_data: SupplierSchema, user_id: int):
    supplier = await supplier_service.create_supplier(supplier_data, user_id)
    return handle_result(supplier)