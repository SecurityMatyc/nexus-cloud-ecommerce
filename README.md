# Nexus of Cloud

Plataforma web académica de comercio electrónico multiempresa para gestionar compañías, usuarios, productos, inventario, ventas y reportes mediante Django.

Proyecto desarrollado durante **2025** para la **Evaluación 4 de Backend**.

## Estado del proyecto

Implementación académica funcional de alcance intermedio. El sistema representa una base de comercio electrónico con separación lógica por empresa, control de roles y flujo de ventas con actualización de inventario.

La versión disponible está orientada a ejecución local y revisión técnica. No debe considerarse una plataforma lista para producción sin completar configuraciones de seguridad, infraestructura y operación.

## Contexto y objetivo

Nexus of Cloud simula un escenario SaaS en el que distintas compañías administran sus operaciones comerciales dentro de una misma plataforma.

El objetivo fue aplicar conceptos de desarrollo backend relacionados con:

- Modelado de entidades comerciales.
- Separación de información por compañía.
- Gestión de usuarios y permisos.
- Administración de inventario.
- Registro de ventas.
- Exposición de endpoints de autenticación mediante JWT.

## Autores

- Matías Gajardo
- Jean Pierre Avastia

Proyecto realizado en equipo como parte del proceso formativo en desarrollo backend.

## Modelo funcional

La plataforma contempla distintos perfiles de usuario:

- `superadmin`: administración general de la plataforma.
- `admin_cliente`: administración de una compañía cliente.
- `gerente`: acceso a información y reportes de gestión.
- `vendedor`: operación de ventas tipo POS.
- `cliente_final`: interacción con el catálogo y el proceso comercial definido por el sistema.

La disponibilidad de cada funcionalidad depende del rol y de los permisos asociados a la vista correspondiente.

## Funcionalidades principales

### Administración multiempresa

- Gestión de compañías y planes.
- Asociación de usuarios con una compañía.
- Organización de la operación comercial por empresa.

### Usuarios y permisos

- Modelo de usuario personalizado.
- Roles diferenciados para cada tipo de operación.
- Control de acceso por vista.
- Autenticación web mediante Django.
- Autenticación de API mediante JWT.

### Catálogo e inventario

- Gestión de productos.
- Registro de proveedores.
- Administración de sucursales.
- Control de existencias por sucursal.
- Actualización de stock asociada al flujo de ventas.

### Ventas y reportes

- Registro de ventas.
- Detalle de productos vendidos.
- Flujo de venta para el perfil vendedor.
- Descuento de stock al completar operaciones.
- Dashboard diferenciado por tipo de usuario.
- Reportes para perfiles administrativos.

## Flujo general de una venta

1. El usuario accede según su rol.
2. El vendedor selecciona los productos disponibles.
3. El sistema registra el detalle de la venta.
4. Se actualiza el inventario de la sucursal correspondiente.
5. La información queda disponible para consulta y reportes según los permisos del usuario.

## Arquitectura y módulos

El proyecto está organizado en aplicaciones Django con responsabilidades separadas:

- `cuentas`: autenticación, usuarios, compañías, planes y roles.
- `productos`: administración del catálogo.
- `proveedores`: gestión de proveedores.
- `inventario`: existencias y sucursales.
- `ventas`: ventas, detalle de ventas y reportes.
- `main`: vistas generales de la plataforma.

## Tecnologías

- Python 3
- Django 5.2
- Django REST Framework
- Simple JWT (`djangorestframework_simplejwt`)
- SQLite para desarrollo local
- HTML, CSS y JavaScript
- Bootstrap

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
| `http://127.0.0.1:8000/` | Sitio web principal |
| `http://127.0.0.1:8000/login/` | Inicio de sesión |
| `http://127.0.0.1:8000/admin/` | Panel de administración Django |

## API de autenticación JWT

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `POST` | `/api/auth/login/` | Inicio de sesión y emisión de tokens |
| `POST` | `/api/auth/refresh/` | Renovación del token de acceso |
| `POST` | `/api/token/` | Obtención de token JWT |
| `POST` | `/api/token/refresh/` | Renovación del token JWT |

## Base de datos y despliegue

La versión disponible utiliza **SQLite** como base de datos de desarrollo. Esto permite ejecutar el proyecto localmente sin depender de servicios externos.

El repositorio representa una base académica preparada para evolucionar hacia entornos de despliegue reales. Antes de utilizarla en un entorno productivo sería necesario configurar una base de datos administrada, variables de entorno, almacenamiento seguro de secretos, HTTPS, políticas de respaldo y controles de acceso adicionales.

## Alcance y limitaciones

El proyecto demuestra una arquitectura funcional para comercio electrónico multiempresa, pero mantiene un alcance académico. Entre sus principales consideraciones se encuentran:

- La configuración local está orientada a desarrollo.
- SQLite no está pensada como base principal para una operación productiva de alta concurrencia.
- Las credenciales y secretos deben gestionarse mediante variables de entorno.
- La separación multiempresa debe validarse mediante pruebas de autorización y aislamiento de datos.
- El flujo de pagos, si se requiere, debería integrarse mediante un proveedor especializado.
- El despliegue productivo requeriría endurecimiento de Django, monitoreo, respaldos y controles de seguridad.

## Contexto académico

Este repositorio corresponde a la Evaluación 4 de Backend. El trabajo permitió aplicar conceptos de arquitectura modular, control de acceso, gestión de inventario, flujo de ventas, organización de aplicaciones Django y autenticación basada en tokens dentro de un escenario de comercio electrónico multiempresa.
