class Login:
    def __init__(self, login: str):
        if len(login) < 8:
            raise MinLengthUserLoginError
        if len(login) > 32:
            raise MaxLengthUserLoginError

        self.login = login
