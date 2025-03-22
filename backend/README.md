# Backend - API de Mis Eventos

Este backend está desarrollado en FastAPI y gestiona usuarios, eventos, sesiones y registros de asistentes.


## ⚙️ Variables de entorno

Crea un archivo `.env`:

```env
DATABASE_URL=postgresql://postgres:postgres@db:5432/mis_eventos
SECRET_KEY=clave-super-secreta
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
