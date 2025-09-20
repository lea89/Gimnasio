from pydantic import BaseModel
from typing import Optional
import datetime

class UserCreate(BaseModel):
    username: str
    password: str
    full_name: Optional[str] = None
    email: Optional[str] = None

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class AlumnoBase(BaseModel):
    nombre: str
    apellido: Optional[str] = None
    dni: Optional[str] = None
    telefono: Optional[str] = None
    email: Optional[str] = None

class AlumnoCreate(AlumnoBase):
    pass

class AlumnoOut(AlumnoBase):
    id: int
    active: bool
    class Config:
        orm_mode = True
