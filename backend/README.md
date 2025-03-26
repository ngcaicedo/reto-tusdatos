# Backend - API de Mis Eventos

Este backend está desarrollado en FastAPI y gestiona usuarios, eventos, sesiones y registros de asistentes.


## ⚙️ Variables de entorno

Crea un archivo `.env`:

```env
DATABASE_USER=
DATABASE_PASSWORD=
DATABASE_NAME=
DATABASE_HOST=
DATABASE_PORT=
SECRETE_KEY=
```
- Puede generar una SECRETE_KEY:  

``` bash
openssl rand -hex 32
```   

## 📦 Estructura del backend

```bash
app/
├── api/         # Rutas 
├── db/          # Config DB y sesiones
├── models/      # Modelos con SQLModel
├── schemas/     # Esquemas Pydantic
├── core/        # Configuraciones y seguridad
├── main.py      # Entrada principal
```

## Funcionalidades implementadas

- **Autenticación de usuarios**
  - Registro y login con validación
  - Manejo de token e inyeccion de dependencia de usuario, tanto obligatoria como opcional

- **Gestión de eventos**
  - Listado de eventos 
  - Detalle de evento 
  - Creación y edición de eventos (sólo autenticados)
  - Registro de usuarios a eventos 

- **Sesiones**
  - Visualización de sesiones por evento
  - Creación y edición para organizadores

- **Perfil**
  - Visualización de eventos registrados
  - CRUD de asistentes para gestionar su información.


## 🧪 Tests

```bash
poetry run pytest
poetry run pytest --cov=app
```

## 🔧 Migraciones

```bash
alembic revision --autogenerate -m "mensaje"
alembic upgrade head
```

## 🔐 Seguridad

- JWT tokens
- Hash de contraseñas (`passlib`)
- Protección de rutas
