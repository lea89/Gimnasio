from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Numeric, Text
from sqlalchemy.orm import relationship
from .database import Base
import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class Alumno(Base):
    __tablename__ = "alumnos"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String)
    dni = Column(String, unique=True, index=True)
    telefono = Column(String)
    email = Column(String, index=True)
    foto_path = Column(String, nullable=True)
    face_encoding = Column(Text, nullable=True)
    active = Column(Boolean, default=True)

class Membresia(Base):
    __tablename__ = "membresias"
    id = Column(Integer, primary_key=True)
    alumno_id = Column(Integer, ForeignKey("alumnos.id"))
    tipo = Column(String)
    precio = Column(Numeric)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    paid = Column(Boolean, default=False)
    alumno = relationship("Alumno")

class Pago(Base):
    __tablename__ = "pagos"
    id = Column(Integer, primary_key=True)
    alumno_id = Column(Integer, ForeignKey("alumnos.id"))
    amount = Column(Numeric)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    method = Column(String)

class Acceso(Base):
    __tablename__ = "accesos"
    id = Column(Integer, primary_key=True)
    alumno_id = Column(Integer, ForeignKey("alumnos.id"))
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    granted = Column(Boolean)
    reason = Column(String, nullable=True)
