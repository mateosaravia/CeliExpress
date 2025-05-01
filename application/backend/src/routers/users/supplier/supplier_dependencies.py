from ....services.users import user_service
from ....utils.exceptions.users.user_exceptions import UserException
from ....data_access.schemas.users.supplier_schema import SupplierSchema

async def valid_supplier_profile(supplier_data: SupplierSchema) -> SupplierSchema:
    user = await user_service.get_user_by_field("id", supplier_data.user_id)
    if user.value == None:
        raise UserException.UserNotFound
    return supplier_data