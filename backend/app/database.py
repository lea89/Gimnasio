import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Tomamos la URL de la variable de entorno
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

# Reemplazamos 'postgres://' por 'postgresql://' si es necesario
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Configuración de SQLite (solo si usamos SQLite)
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

# Creamos el engine de SQLAlchemy
engine = create_engine(DATABASE_URL, connect_args=connect_args, pool_pre_ping=True)

# Creamos la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base declarativa para los modelos
Base = declarative_base()
