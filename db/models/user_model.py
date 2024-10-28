# app/db/models/user.py

from sqlalchemy import Column, Integer, String
from db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)  # Nome completo
    email = Column(String, unique=True, index=True)  # Email
    cpf = Column(String, unique=True, index=True)  # CPF
    address = Column(String)  # Endereço
    hashed_password = Column(String)  # Senha
