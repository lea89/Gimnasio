from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import crud, schemas, auth
from ..deps import get_db
from ..auth import get_current_user

router = APIRouter()

@router.post("/register", response_model=dict)
def register(user: schemas.UserCreate, db: Session = Depends(get_db), current=Depends(get_current_user)):
    existing = crud.get_user_by_username(db, user.username)
    if existing:
        return {"error":existing}
        raise HTTPException(status_code=400, detail="username already registered")
    new = crud.create_user(db, user, is_admin=True)
    return {"username": new.username, "id": new.id,"error":existing}

@router.post("/token", response_model=schemas.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    access_token = auth.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
