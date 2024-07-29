class UserError(Exception):
    """Базовое исключение для пользователей"""


class MinLengthUserLoginError(UserError):

    def __init__(self, msg='User has a login less than the minimum.'):
        super().__init__(msg)


class MaxLengthUserLoginError(UserError):

    def __init__(self, msg='User has a login greater than the maximum.'):
        super().__init__(msg)


class MinLengthUserFirstNameError(UserError):

    def __init__(self, msg='User has a first name less than the minimum.'):
        super().__init__(msg)


class MaxLengthUserFirstNameError(UserError):

    def __init__(self, msg='User has a first name greater than the maximum.'):
        super().__init__(msg)


class MinLengthUserSecondNameError(UserError):

    def __init__(self, msg='User has a second name less than the minimum.'):
        super().__init__(msg)


class MaxLengthUserSecondNameError(UserError):

    def __init__(self, msg='User has a second name greater than the maximum.'):
        super().__init__(msg)


class IncorrectEmailError(UserError):

    def __init__(self, msg='Email was written with an error.'):
        super().__init__(msg)


class UserNotFoundError(UserError):

    def __init__(self, msg='User not found.'):
        super().__init__(msg)


class UserExistsError(UserError):

    def __init__(self, msg='User already exists.'):
        super().__init__(msg)
