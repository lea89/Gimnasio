from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud
from ..deps import get_db
from ..auth import get_current_user

router = APIRouter()

@router.post("/", response_model=schemas.AlumnoOut)
def create_alumno(alumno: schemas.AlumnoCreate, db: Session = Depends(get_db), current=Depends(get_current_user)):
    return crud.create_alumno(db, alumno)

@router.get("/", response_model=list[schemas.AlumnoOut])
def list_alumnos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current=Depends(get_current_user)):
    return crud.get_alumnos(db, skip=skip, limit=limit)

@router.get("/{alumno_id}", response_model=schemas.AlumnoOut)
def get_alumno(alumno_id: int, db: Session = Depends(get_db), current=Depends(get_current_user)):
    db_al = crud.get_alumno(db, alumno_id)
    if not db_al:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")
    return db_al
