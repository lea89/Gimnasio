from fastapi import FastAPI
from .database import engine, Base
from .routers import auth, alumnos

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Gimnasio MVP")


@app.get("/health")
def health_check():
    return {"status": "Render backend is running!"}

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(alumnos.router, prefix="/alumnos", tags=["alumnos"])
