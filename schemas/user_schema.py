# app/schemas/user.py

from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    full_name: str  # Nome completo
    email: EmailStr  # Email com validação
    cpf: str  # CPF
    address: str  # Endereço

class UserCreate(UserBase):
    password: str  # Campo para a senha que será enviada na criação

class UserResponse(UserBase):
    id: int  # ID do usuário

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: str
    password: str