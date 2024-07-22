from dotenv import load_dotenv
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings

load_dotenv()


class DatabaseSettings(BaseSettings):
    """
    Настройки к базе данных.

    Attributes:
        postgres_url: Строка подключения к PostgreSQL.
        # redis_url: Строка подключения к Redis.
    """
    postgres_url: PostgresDsn
    # redis_url: RedisDsn


class AuthenticationSettings(BaseSettings):
    """
    Настройки аутентификации.

    Attributes:
        access_secret_key: Секретный ключ для генерации токенов доступа.
        access_expiration: Время жизни токенов доступа в минутах.
        refresh_secret_key: Секретный ключ для генерации токенов обновления.
        refresh_expiration: Время жизни токенов обновления в минутах.
        jwt_algorithm: Алгоритм кодирования токена.
        password_salt: Соль для хеширования пароля пользователя.
        iters_hashing: Количество итераций для хеширования пароля пользователя.
        hash_algorithm: Алгоритм для хеширования пароля пользователя.
    """
    access_secret_key: str
    access_expiration: int
    refresh_secret_key: str
    refresh_expiration: int
    jwt_algorithm: str
    password_salt: str
    iters_hashing: int
    hash_algorithm: str

