from pydantic_settings import BaseSettings
from pydantic import HttpUrl, EmailStr, SecretStr


class Settings(BaseSettings):
    # Application Settings
    TITLE: str
    DESCRIPTION: str
    VERSION: str
    TERMS_OF_SERVICE: str
    CONTACT_NAME: str
    CONTACT_EMAIL: EmailStr
    CONTACT_URL: HttpUrl
    DOCS_URL: str

    # Auth Settings
    JWT_SECRET_KEY: SecretStr
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    # GRPC Addresses
    AUTH_GRPC_ADDRESS: str


settings = Settings()
