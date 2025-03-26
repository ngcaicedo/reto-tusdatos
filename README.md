# Mis Eventos - Plataforma de Gestión de Eventos

Proyecto Full Stack desarrollado como prueba técnica para TusDatos.co. Esta plataforma permite gestionar eventos, sesiones, ponentes y asistentes de manera eficiente.

## 🧱 Estructura del Proyecto

```bash
reto-eventos/
├── backend/   # FastAPI + PostgreSQL + Alembic + TDD
├── frontend/  # Angular + TDD
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
- Frontend: http://localhost:4200/events
- Se tiene un usuario por defecto que puede crear usuario organizadores y también crear eventos, sesiones y ponentes:
    - username: admin@gmail.com
    - password: admin
- No olvidar crear el archivo .env en el backend como el env_example, para poder guardar variables de conexion de base de datos


## 📁 Documentación por módulo

- 🔙 [Backend (FastAPI)](./backend/README.md)
- 🔜 [Frontend (Angular)](./frontend/README.md)

## ✅ Funcionalidades principales

- Creación de eventos y sesiones
- Registro y autenticación de usuarios
- Inscripción de asistentes a eventos
- Ver eventos y su respectivo detalle

## 🧪 Tests

```bash
# Ejecutar solo los tests del backend
cd backend
poetry run pytest --cov=app
```

```bash
# Ejecutar solo los tests del backend
cd frontend
ng test --watch=false --browsers=ChromeHeadless 
```

## 🧠 Tecnologías usadas

- FastAPI, SQLModel, PostgreSQL, Alembic
- Angular, Bootstrap
- Docker, Docker Compose
- Pytest, Faker, Poetry

## 📌 Autor

**Nicolás Caicedo** – Desarrollador Full Stack
