# core/config.py

from pydantic_settings import BaseSettings 


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://tharlles_admin:LiLEXXhP2727@localhost:5432/gifinddb"

    JWT_SECRET: str = "62de3c1bf598e60d868d50679254ebf1"  # Use um valor seguro para produção
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    class Config:
        env_file = ".env"  # Se você usar um arquivo .env para gerenciar variáveis de ambiente

settings = Settings()
