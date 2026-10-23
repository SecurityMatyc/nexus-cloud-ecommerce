# Nexus of Cloud

Plataforma web académica de comercio electrónico multiempresa, orientada a la gestión de ventas, inventario, usuarios y roles mediante Django.

Proyecto académico desarrollado durante **2025** para la **Evaluación 4 de Backend**.

## Autores

- Matías Gajardo
- Jean Pierre Avastia

Proyecto realizado en equipo como parte del proceso formativo en desarrollo backend.

## Descripción del proyecto

Nexus of Cloud simula una plataforma e-commerce con estructura multiempresa. Cada compañía puede administrar su operación comercial mediante usuarios con distintos roles, productos, proveedores, sucursales, inventario y ventas.

El sistema incluye gestión de:

- Compañías y planes.
- Usuarios por rol: `superadmin`, `admin_cliente`, `gerente`, `vendedor` y `cliente_final`.
- Productos y proveedores.
- Sucursales e inventario por sucursal.
- Ventas y detalle de ventas para operación tipo POS.
- Reportes de ventas para perfiles administrativos.

Además de la interfaz web basada en plantillas Django, el proyecto expone endpoints de autenticación mediante JWT con Django REST Framework.

## Características principales

- Arquitectura modular organizada en aplicaciones Django.
- Modelo de usuario personalizado con roles y permisos por vista.
- Operaciones CRUD para los módulos principales.
- Flujo de ventas con descuento de stock en inventario.
- Dashboard diferenciado según el tipo de usuario.
- API REST de autenticación con JWT para inicio y renovación de sesión.
- Interfaz web con plantillas Django y Bootstrap.

## Tecnologías

- Python 3
- Django 5.2
- Django REST Framework
- Simple JWT (`djangorestframework_simplejwt`)
- SQLite para desarrollo
- HTML, CSS y JavaScript
- Bootstrap

## Módulos del sistema

- `cuentas`: autenticación, usuarios y roles.
- `productos`: administración de productos.
- `proveedores`: gestión de proveedores.
- `inventario`: existencias y sucursales.
- `ventas`: ventas, detalle de ventas y reportes.
- `main`: vistas generales de la plataforma.

## Puesta en marcha local

### 1. Clonar el repositorio

```powershell
git clone <url-del-repositorio>
cd <nombre-del-repositorio>
```

### 2. Crear y activar el entorno virtual

```powershell
python -m venv env
.\env\Scripts\Activate.ps1
```

### 3. Instalar dependencias

```powershell
pip install -r requirements.txt
```

### 4. Crear y aplicar migraciones

```powershell
python manage.py makemigrations
python manage.py migrate
```

### 5. Iniciar el servidor

```powershell
python manage.py runserver
```

## Rutas principales

| Ruta | Descripción |
|------|-------------|
| `http://127.0.0.1:8000/` | Sitio web |
| `http://127.0.0.1:8000/login/` | Inicio de sesión |
| `http://127.0.0.1:8000/admin/` | Panel de administración Django |

## Endpoints de autenticación JWT

- `POST /api/auth/login/`
- `POST /api/auth/refresh/`
- `POST /api/token/`
- `POST /api/token/refresh/`

## Despliegue y alcance

El proyecto fue desarrollado como una base académica preparada para evolucionar hacia entornos de despliegue reales. La versión disponible está configurada principalmente para ejecución local con SQLite.

## Contexto académico

Este repositorio conserva una entrega de la Evaluación 4 de Backend. Su objetivo fue aplicar conceptos de desarrollo web, arquitectura modular, control de acceso, gestión de inventario, flujo de ventas y autenticación basada en tokens dentro de un escenario e-commerce multiempresa.
