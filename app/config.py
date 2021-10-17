from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str
    TOKEN: str

    SQLALCHEMY_DATABASE_URI: str

    class Config:
        case_sensitive = True
        env_file = '.env'


settings = Settings()
