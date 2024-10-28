from sqlalchemy.orm import Session
from typing import Generator
from .base import SessionLocal  # Importando corretamente

# Dependência para uso de sessão no FastAPI
def get_db() -> Generator[Session, None, None]:  # Especificando o tipo de retorno como Generator
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
