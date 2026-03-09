# Nexus of Cloud ☁️🛒
Proyecto academico desarrollado durante 2025 para la Evaluacion 4 de Backend.

Este sistema representa una plataforma ficticia de comercio electronico multiempresa llamada **Nexus of Cloud**, enfocada en la gestion de ventas, inventario y operacion comercial por roles.

## 👥 Autores
- Matias Gajardo
- Jean Pierre Avastia

Trabajo realizado en conjunto como parte del proceso formativo en desarrollo backend.

## 🧩 Descripcion del proyecto
La aplicacion simula un entorno e-commerce basico con estructura SaaS (multiempresa), donde cada compania puede administrar su operacion comercial.

Incluye gestion de:

- Companias y planes
- Usuarios por rol (superadmin, admin_cliente, gerente, vendedor, cliente_final)
- Productos
- Proveedores
- Sucursales
- Inventario por sucursal
- Ventas y detalle de ventas (POS vendedor)
- Reportes de ventas para perfiles administrativos

Ademas de la gestion web con Django Templates, el proyecto expone endpoints API para autenticacion JWT con Django REST Framework.

## ✨ Caracteristicas principales
- Arquitectura modular por apps Django (`cuentas`, `productos`, `proveedores`, `inventario`, `ventas`, `main`)
- Modelo de usuario personalizado con roles y permisos por vista
- CRUD para modulos clave del negocio
- Flujo de ventas con descuento de stock en inventario
- Dashboard diferenciado por tipo de usuario
- API REST de autenticacion con JWT (login y refresh)
- Interfaz web con plantillas Django y Bootstrap

## 🛠️ Stack tecnologico
- Python 3
- Django 5.2
- Django REST Framework
- Simple JWT (`djangorestframework_simplejwt`)
- SQLite (entorno de desarrollo)
- HTML, CSS, JS, Bootstrap

## 🗂️ Modulos del sistema
- Cuentas y autenticacion
- Companias y planes
- Productos
- Proveedores
- Inventario y sucursales
- Ventas y reportes

## 🚀 Puesta en marcha local
1. Clonar el repositorio.
2. Entrar a la carpeta del proyecto.
3. Crear y activar entorno virtual (si aun no existe).
4. Instalar dependencias.
5. Aplicar migraciones.
6. Iniciar servidor.

Comandos sugeridos en Windows PowerShell:

```powershell
python -m venv env
.\env\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Abrir en navegador:

- `http://127.0.0.1:8000/` (sitio web)
- `http://127.0.0.1:8000/login/` (login principal)
- `http://127.0.0.1:8000/admin/` (panel admin Django)

Endpoints API de autenticacion JWT:

- `http://127.0.0.1:8000/api/auth/login/`
- `http://127.0.0.1:8000/api/auth/refresh/`
- `http://127.0.0.1:8000/api/token/`
- `http://127.0.0.1:8000/api/token/refresh/`

## ☁️ Despliegue
Como parte del trabajo academico, el proyecto considera una base preparada para evolucionar a entornos de despliegue reales.

## 🎯 Contexto academico
Este repositorio conserva una entrega importante del curso para poder revisar decisiones, estructura y avances logrados durante la Evaluacion 4.

En resumen: una base solida de backend orientada a e-commerce multiempresa, desarrollada en equipo y con valor como referencia para proyectos futuros.
