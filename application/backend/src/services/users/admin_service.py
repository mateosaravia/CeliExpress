from ...schemas.users.admin_schema import AdminSchema

def add_admin(admin):
    new_admin = AdminSchema(**admin)
    return new_admin