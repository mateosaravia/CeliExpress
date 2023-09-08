from ...schemas.users.supplier_schema import SupplierSchema

def add_supplier(supplier):
    new_supplier = SupplierSchema(**supplier)
    return new_supplier
