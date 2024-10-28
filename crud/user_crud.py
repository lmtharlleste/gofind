# app/crud/user.py
from sqlalchemy.orm import Session
from db.models.user_model import User
from schemas.user_schema import UserCreate
from passlib.context import CryptContext

# Inicializa o contexto do Passlib para criptografar senhas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(db: Session, user: UserCreate):
    hashed_password = pwd_context.hash(user.password)  # Criptografa a senha
    db_user = User(
        full_name=user.full_name,
        email=user.email,
        cpf=user.cpf,
        address=user.address,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()
