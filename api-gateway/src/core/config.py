from pydantic_settings import BaseSettings
from pydantic import HttpUrl, EmailStr


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

    # GRPC Addresses
    AUTH_GRPC_ADDRESS: str


settings = Settings()
