dummy_db = {}

async def add_user_to_db(user):
    dummy_db[user.email] = user
    return user

async def get_user_by_email(email):
    return dummy_db.get(email)