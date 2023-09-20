from ...data_access.schemas.users.supplier_schema import SupplierSchema
from ...data_access.repositories.users import supplier_repository
from ...utils.results.result_handler import Result
from ...utils.exceptions.users.supplier_exceptions import SupplierException

async def create_supplier_profile(supplier_data):
    user_id = supplier_data.user_id
    exists = await supplier_repository.get_supplier_profile(user_id)
    if exists:
        return Result(SupplierException.SupplierProfileAlreadyExists())

    added_profile = await supplier_repository.add_supplier_profile(supplier_data)

    return Result(added_profile)