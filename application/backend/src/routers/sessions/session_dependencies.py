from ...utils.exceptions.sessions.session_exceptions import SessionException

async def valid_user_login(login_data):
    pass

async def valid_user_token(authorizationHeader):
    if authorizationHeader is None:
        raise SessionException.InvalidToken

    token = authorizationHeader.split(" ")[1]
    return token