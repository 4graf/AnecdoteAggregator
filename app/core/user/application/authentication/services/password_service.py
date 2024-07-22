import hashlib

from app.settings import AuthenticationSettings

settings = AuthenticationSettings()


class PasswordService:
    @classmethod
    def hash_password(cls, password: str) -> str:
        hashed = hashlib.pbkdf2_hmac(settings.hash_algorithm,
                                     password.encode(),
                                     settings.password_salt.encode(),
                                     settings.iters_hashing)
        return hashed.hex()

    @classmethod
    def validate_password(cls, login_password, hashed_password: str) -> bool:
        return cls.hash_password(login_password) == hashed_password
