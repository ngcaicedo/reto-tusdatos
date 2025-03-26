# Frontend - Aplicación "Mis Eventos"

Este documento describe la arquitectura, configuración y principales decisiones técnicas tomadas para el desarrollo del **frontend** de la aplicación "Mis Eventos", desarrollada como parte del reto técnico de TusDatos.co.

## Tecnologías utilizadas

- **Framework**: Angular 19
- **Node.js**: v20
- **Librerías adicionales**:
  - @angular/router (enrutamiento)
  - RxJS (programación reactiva)
  - ng Bootstrap 
  - ngx-toastr (notificaciones)

## Estructura del proyecto

```bash
src/
├── app/
│   ├── auth-user/         # login y registro de usuarios
│   ├── event-managment/   # Manejador de las acciones de los eventos
│   ├── header/            # Estrucutura común
│   ├── session-managment/ # Manejador de las acciones de las sesiones y ponentes
│   ├── shared             # compartido como guard, interceptors, spinner etc..
│   └── app.component.ts   # Componente principal
│   └── app.routes.ts      # Rutas de las páginas
```

## Funcionalidades implementadas

- **Autenticación de usuarios**
  - Registro y login con validación
  - Manejo de token y persistencia en localStorage
  - Protección de rutas con `AuthGuard` y `RoleGuard`

- **Gestión de eventos**
  - Listado de eventos
  - Detalle de evento (incluye sesiones)
  - Creación de eventos (sólo autenticados)
  - Registro de usuarios a eventos 

- **Sesiones**
  - Visualización de sesiones por evento
  - Creación para organizadores

- **Perfil**
  - Visualización de eventos registrados



## Seguridad

- Las rutas protegidas usan `AuthGuard` para validar autenticación
- `RoleGuard` verifica los roles para acceso a funcionalidades específicas
- El token JWT se adjunta a cada petición usando un `HttpInterceptor`
- Validaciones de formularios (front y backend)

## Buenas prácticas

- Arquitectura basada en features + core/shared
- Componentes standalone para mayor reutilización
- Lazy loading para mejorar el rendimiento
- Naming consistente y uso de tipado fuerte (TypeScript)

## Tests

- Se implementaron pruebas unitarias con `@angular/core/testing`
- Cobertura para componentes, servicios y guards
- Mocking de servicios HTTP con `HttpTestingController`

## Instalación y ejecución

```bash
npm install
npm run start
```

## Variables de entorno

Las variables necesarias se encuentran en `environment.ts`, incluyendo:

- `API_BASE_URL`: URL base del backend

## Mejoras futuras

- Integrar cache con SWR o Apollo
- Mejorar cobertura de pruebas
- Implementar accesibilidad (a11y)
- Implementar paginación de los eventos

---

**Autor**: Nicolas Caicedo  
**Fecha**: Marzo 2025  
**Proyecto**: Reto técnico TusDatos.co