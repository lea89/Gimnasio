# Gimnasio MVP - Quickstart

## Qué incluye
- Backend: FastAPI + SQLAlchemy (endpoints mínimos: register, token, alumnos CRUD)
- Frontend: React (Vite) minimal (Login + Alumnos)
- docker-compose para levantar DB (Postgres), backend y frontend localmente

## Levantar local con Docker (recomendado)
1. Copiar `.env.example` a `.env` y ajustar valores.
2. `docker-compose up --build`
3. Backend: http://localhost:8000/docs
4. Frontend: http://localhost:3000

## Notas
- El servicio de reconocimiento facial no está compilado ni incluido como dependencia automática (libros pesados). En `backend/app` hay espacio para `face_service.py` si querés integrar `face_recognition`.
- Para producción recomendamos usar una base de datos gestionada (Aiven, Supabase) y desplegar backend en Render / Railway / Fly.io (ver guía en el README principal).
