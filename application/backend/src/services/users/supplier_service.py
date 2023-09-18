from ...data_access.schemas.users.supplier_schema import SupplierSchema
from ...data_access.repositories.users import supplier_repository
from ...utils.results.results_handler import ServiceResult
from ...utils.exceptions.users.supplier_exceptions import SupplierException

async def create_supplier_profile(supplier_data, user_id):
    exists = get_profile_by_user(user_id)
    if exists:
        return ServiceResult(SupplierException.SupplierProfileAlreadyExists())

    new_profile = SupplierSchema(**supplier_data)
    added_profile = supplier_repository.add_supplier_profile(new_profile, user_id)

    return ServiceResult(added_profile)