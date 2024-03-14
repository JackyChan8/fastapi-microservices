from pydantic import SecretStr, PostgresDsn
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Postgresql database settings
    DATABASE_PROTOCOL: str = 'postgresql'
    DATABASE_PASSWORD: SecretStr
    DATABASE_URL: str = ""
    DATABASE_NAME: str
    DATABASE_USER: str
    DATABASE_HOST: str
    DATABASE_PORT: int

    # Auth Settings
    JWT_SECRET_KEY: SecretStr
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    def get_database_url(self):
        return PostgresDsn.build(
            scheme=self.DATABASE_PROTOCOL,
            username=self.DATABASE_USER,
            password=self.DATABASE_PASSWORD.get_secret_value(),
            host=self.DATABASE_HOST,
            port=self.DATABASE_PORT,
            path=self.DATABASE_NAME,
        )


settings = Settings()
