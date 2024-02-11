from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    title: str = "quiz"
    # TODO: rename
    url: str = "https://the-trivia-api.com/v2/questions"
    POSTGRES_USER: str
    POSTGRES_DB: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    SQLALCHEMY_DATABASE_URL: str
    model_config = SettingsConfigDict(
        env_file=".env",
    )


settings = Settings()
