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


class JWTSettings(BaseSettings):
    """
    Настройки JWT.

    Attributes:
        access_secret_key: Секретный ключ для генерации токенов доступа.
        access_expiration: Время жизни токенов доступа в минутах.
        refresh_secret_key: Секретный ключ для генерации токенов обновления.
        refresh_expiration: Время жизни токенов обновления в минутах.
        algorithm: Алгоритм кодирования токена.
    """
    access_secret_key: str
    access_expiration: int
    refresh_secret_key: str
    refresh_expiration: int
    algorithm: str
