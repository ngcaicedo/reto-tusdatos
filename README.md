# Mis Eventos - Plataforma de Gestión de Eventos

Proyecto Full Stack desarrollado como prueba técnica para TusDatos.co. Esta plataforma permite gestionar eventos, sesiones, ponentes y asistentes de manera eficiente.

## 🧱 Estructura del Proyecto

```bash
reto-eventos/
├── backend/   # FastAPI + PostgreSQL + Alembic + TDD
├── frontend/  # Angular
├── docker-compose.yml
└── README.md
```

## 🚀 ¿Cómo levantar el proyecto completo?

Asegúrate de tener Docker y Docker Compose instalados.

```bash
docker-compose up --build
```

La aplicación estará disponible en:
- API: http://localhost:8000/docs
- Frontend: http://localhost:4200 

## 📁 Documentación por módulo

- 🔙 [Backend (FastAPI)](./backend/README.md)
- 🔜 [Frontend (Angular)](./frontend/README.md)

## ✅ Funcionalidades principales

- Gestión de eventos y sesiones
- Registro y autenticación de usuarios
- Inscripción de asistentes a eventos
- Validación de capacidad y horarios

## 🧪 Tests

```bash
# Ejecutar solo los tests del backend
cd backend
poetry run pytest --cov=app
```

## 🧠 Tecnologías usadas

- FastAPI, SQLModel, PostgreSQL, Alembic
- Angular, RxJS, Angular Router
- Docker, Docker Compose
- Pytest, Faker, Poetry

## 📌 Autor

**Nicolás Caicedo** – Desarrollador Full Stack
