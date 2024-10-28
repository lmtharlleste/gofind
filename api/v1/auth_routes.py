from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from crud.user_crud import get_user_by_email
from schemas.user_schema import UserLogin
from core.security import create_access_token  # Função para criar JWT
from passlib.context import CryptContext

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    # Busca o usuário pelo email
    db_user = get_user_by_email(db, email=user.email)
    
    # Verifica se o usuário existe e se a senha está correta
    if not db_user or not pwd_context.verify(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    # Gera o token de acesso (JWT) com o email do usuário
    access_token = create_access_token(data={"sub": db_user.email})
    
    return {"access_token": access_token, "token_type": "bearer"}
