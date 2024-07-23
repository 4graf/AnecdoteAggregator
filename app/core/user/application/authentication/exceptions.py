class AuthenticationError(Exception):
    """Базовое исключение для пользователей"""


class WrongPasswordError(AuthenticationError):

    def __init__(self, msg='Incorrect entry of credentials.'):
        super().__init__(msg)


class TokenExpiredException(AuthenticationError):

    def __init__(self, msg='The token has expired.'):
        super().__init__(msg)


class TokenCorruptedException(AuthenticationError):

    def __init__(self, msg='The token is corrupted.'):
        super().__init__(msg)

