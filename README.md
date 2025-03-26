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

# Arquitectura 
## Diagrama de componentes
![reto-tusdatos drawio (1)](https://github.com/user-attachments/assets/181af085-5fdf-4ab0-8efe-fdb617a5ef23)

## Diagrama de clases
![image](https://github.com/user-attachments/assets/20e14714-83fa-44d2-97df-3a26ea9cd5d5)

# User Story Map
![USM - TusDatos (1)](https://github.com/user-attachments/assets/f49c3859-333c-4b03-b44d-294c06182512)

# Mockups
![UI Diseño Mis eventos RETO](https://github.com/user-attachments/assets/0ef2706d-d33d-476c-9118-a03b0b2006c4)


## 📌 Autor

**Nicolás Caicedo** – Desarrollador Full Stack
