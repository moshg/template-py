from typing import Literal

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    log_format: Literal["console", "json"] = "console"


settings = Settings()
