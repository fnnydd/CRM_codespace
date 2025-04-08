from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path
from dotenv import load_dotenv
from pydantic import SecretStr

BASE_DIR: Path = Path(__file__).parent.parent.parent
ENV_FILE_PATH: Path = BASE_DIR / ".env"


if not ENV_FILE_PATH.exists():
    raise FileNotFoundError(f"Файл {ENV_FILE_PATH} не найден!")

load_dotenv(ENV_FILE_PATH)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(extra="ignore", env_file=ENV_FILE_PATH)

    POSTGRES_DB: SecretStr
    POSTGRES_USER: SecretStr
    POSTGRES_PASSWORD: SecretStr
    POSTGRES_HOST: SecretStr
    POSTGRES_PORT: int
    @property
    def DATABASE_URL(self) -> str:
        return (
            "postgresql+asyncpg://"
            f"{self.POSTGRES_USER.get_secret_value()}:{self.POSTGRES_PASSWORD.get_secret_value()}"
            f"@{self.POSTGRES_HOST.get_secret_value()}:{self.POSTGRES_PORT}/{self.POSTGRES_DB.get_secret_value()}"
        )