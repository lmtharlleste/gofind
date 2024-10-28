# app/api/v1/users.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from crud.user_crud import create_user, get_user_by_email
from schemas.user_schema import UserCreate, UserResponse

router = APIRouter()

@router.post("/users/", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    return create_user(db=db, user=user)