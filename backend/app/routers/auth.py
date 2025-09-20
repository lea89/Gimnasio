from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from .. import crud, schemas, auth
from ..deps import get_db
from ..auth import get_current_user

router = APIRouter()

@router.post("/register", response_model=dict)
def register(user: schemas.UserCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    existing = crud.get_user_by_username(db, user.username)
    from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from . import models, schemas
from .database import get_db
from .security import hash_password  # tu función de hash

def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Crear el usuario
    new_user = models.User(
        username=user.username,
        email=user.email,
        full_name=user.full_name,
        hashed_password=hash_password(user.password)
    )
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except IntegrityError as e:
        db.rollback()
        # Revisar si la violación fue por email o username
        if 'email' in str(e.orig):
            raise HTTPException(status_code=400, detail="Email already registered")
        elif 'username' in str(e.orig):
            raise HTTPException(status_code=400, detail="Username already registered")
        else:
            raise HTTPException(status_code=400, detail="User already exists")
    return new_user


@router.post("/token", response_model=schemas.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    access_token = auth.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
