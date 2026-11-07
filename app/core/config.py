from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    APP_NAME: str = "Report Analyzer API"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False

    DATABASE_HOST: str
    DATABASE_PORT: int = 3306
    DATABASE_USER: str
    DATABASE_PASSWORD: str = ""
    DATABASE_NAME: str

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=False, extra="ignore"
    )


settings = Settings()
