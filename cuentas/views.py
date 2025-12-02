from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponse
from main.models import Compania
from productos.models import Producto
from inventario.models import Sucursal, Inventario
from proveedores.models import Proveedor
from .models import Usuario

# ===========================
# LOGOUT
# ===========================
def user_logout(request):
    logout(request)
    return redirect('/')


# ===========================
# LOGIN
# ===========================
def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard_redirect')
        else:
            return render(request, 'cuentas/login.html', {'error': 'Credenciales inválidas'})

    return render(request, 'cuentas/login.html')


# ===========================
# REDIRIGIR SEGÚN ROL
# ===========================
@login_required(login_url='/accounts/login/')
def dashboard_redirect(request):
    user = request.user

    print("DEBUG ROL:", user.rol)

    if user.rol == 'superadmin':
        return redirect('dashboard_superadmin')

    if user.rol == 'admin_cliente':
        return redirect('dashboard_admin_cliente')

    if user.rol == 'gerente':
        return redirect('gerente_dashboard')

    if user.rol == 'vendedor':
        return redirect('dashboard_vendedor')

    return HttpResponse("Rol desconocido.")



# ===========================
# DASHBOARD SUPERADMIN
# ===========================
@login_required
def dashboard_superadmin(request):
    if request.user.rol != 'superadmin':
        return HttpResponseForbidden("No tienes permiso para acceder aquí.")
    
    total_companias = Compania.objects.count()
    total_usuarios = Usuario.objects.count()
    total_planes = 3  # Básico, Estándar, Premium
    
    return render(request, "cuentas/superadmin_dashboard.html", {
        "total_companias": total_companias,
        "total_usuarios": total_usuarios,
        "total_planes": total_planes
    })



# ===========================
# DASHBOARD ADMIN CLIENTE
# ===========================
@login_required
def dashboard_admin_cliente(request):
    if request.user.rol != 'admin_cliente':
        return HttpResponseForbidden("No tienes permiso para acceder aquí.")
    # Mostrar solo la compañía asignada al usuario (tenant)
    compania = getattr(request.user, 'compania', None)

    if not compania:
        return HttpResponse("No hay compañía asignada a tu usuario. Pide al superadmin que te asigne una.")

    return render(request, "cuentas/admin_cliente_dashboard.html", {"compania": compania})






# ================================
#  LISTAR COMPAÑÍAS
# ================================
@login_required
def companias_listar(request):
    if request.user.rol != 'superadmin':
        return HttpResponseForbidden("No tienes permiso para acceder aquí.")

    companias = Compania.objects.all()
    return render(request, "cuentas/listar_compania.html", {"companias": companias})


# ================================
#  CREAR COMPAÑÍA
# ================================
@login_required
def compania_crear(request):
    if request.user.rol != 'superadmin':
        return HttpResponseForbidden("No tienes permiso para acceder aquí.")

    if request.method == "POST":
        nombre = request.POST.get("nombre")
        rut = request.POST.get("rut")
        direccion = request.POST.get("direccion")
        telefono = request.POST.get("telefono")

        Compania.objects.create(
            nombre=nombre,
            rut=rut,
            direccion=direccion,
            telefono=telefono
        )

        return redirect("compania_listar")

    return render(request, "cuentas/crear_compania.html")


# ================================
#  LISTAR USUARIOS
# ================================
@login_required
def usuarios_listar(request):
    if request.user.rol != 'superadmin':
        return HttpResponseForbidden("No tienes permiso para acceder aquí.")

    usuarios = Usuario.objects.all()
    return render(request, "cuentas/listar_usuarios.html", {"usuarios": usuarios})


# ================================
#  CREAR USUARIO
# ================================
@login_required
def usuario_crear(request):
    if request.user.rol != 'superadmin':
        return HttpResponseForbidden("No tienes permiso para acceder aquí.")

    if request.method == "POST":
        email = (request.POST.get("email") or "").strip().lower()
        nombre = (request.POST.get("nombre") or "").strip()
        password = request.POST.get("password") or ""
        rol = request.POST.get("rol")
        compania_id = request.POST.get("compania")

        # Validaciones básicas
        companias = Compania.objects.all()
        if not email or not nombre or not password or not rol:
            return render(request, "cuentas/crear_usuario.html", {"error": "Rellena todos los campos obligatorios.", "roles": ["superadmin","admin_cliente","gerente","vendedor","cliente_final"], "companias": companias})

        if Usuario.objects.filter(email=email).exists():
            return render(request, "cuentas/crear_usuario.html", {"error": "Email ya registrado.", "roles": ["superadmin","admin_cliente","gerente","vendedor","cliente_final"], "companias": companias})

        compania = None
        if compania_id:
            try:
                compania = Compania.objects.get(pk=compania_id)
            except Compania.DoesNotExist:
                compania = None

        # Crear usuario y asignar compañía en la misma operación (si existe)
        user_kwargs = {
            'email': email,
            'nombre': nombre,
            'password': password,
            'rol': rol,
        }
        if compania:
            user_kwargs['compania'] = compania

        Usuario.objects.create_user(**user_kwargs)

        return redirect("usuario_listar")

    companias = Compania.objects.all()
    return render(request, "cuentas/crear_usuario.html", {"roles": ["superadmin","admin_cliente","gerente","vendedor","cliente_final"], "companias": companias})





# ================================
# ADMIN CLIENTE — CREAR USUARIOS
# ================================
@login_required
def admin_usuarios_listar(request):
    if request.user.rol != 'admin_cliente':
        return HttpResponseForbidden("No tienes permiso.")
    
    compania = request.user.compania
    if not compania:
        return HttpResponse("No hay compañía asignada.")
    
    usuarios = Usuario.objects.filter(compania=compania)
    return render(request, "cuentas/admin_usuarios_listar.html", {"usuarios": usuarios, "compania": compania})


@login_required
def admin_usuarios_crear(request):
    if request.user.rol != 'admin_cliente':
        return HttpResponseForbidden("No tienes permiso.")
    
    compania = request.user.compania
    if not compania:
        return HttpResponse("No hay compañía asignada.")
    
    if request.method == "POST":
        email = (request.POST.get("email") or "").strip().lower()
        nombre = (request.POST.get("nombre") or "").strip()
        password = request.POST.get("password") or ""
        rol = request.POST.get("rol") or "vendedor"
        
        if not email or not nombre or not password:
            return render(request, "cuentas/admin_usuarios_crear.html", 
                         {"error": "Rellena todos los campos obligatorios.", "compania": compania})
        
        if Usuario.objects.filter(email=email).exists():
            return render(request, "cuentas/admin_usuarios_crear.html", 
                         {"error": "Email ya registrado.", "compania": compania})
        
        Usuario.objects.create_user(
            email=email,
            nombre=nombre,
            password=password,
            rol=rol,
            compania=compania
        )
        return redirect("admin_usuarios_listar")
    
    return render(request, "cuentas/admin_usuarios_crear.html", {"compania": compania})

@login_required
def gerente_dashboard(request):
    if request.user.rol != "gerente":
        return render(request, "errors/403.html", status=403)

    return render(request, "cuentas/gerente_dashboard.html")

@login_required
def usuario_eliminar(request, id):
    if request.user.rol != "superadmin":
        return HttpResponseForbidden("No tienes permiso.")

    try:
        usuario = Usuario.objects.get(id=id)
    except Usuario.DoesNotExist:
        return HttpResponse("Usuario no encontrado.")

    usuario.delete()
    return redirect("usuario_listar")


@login_required
def compania_eliminar(request, id):
    if request.user.rol != "superadmin":
        return HttpResponseForbidden("No tienes permiso.")

    try:
        compania = Compania.objects.get(id=id)
    except Compania.DoesNotExist:
        return HttpResponse("Compañía no encontrada.")

    compania.delete()
    return redirect("compania_listar")

@login_required
def dashboard_vendedor(request):
    if request.user.rol != "vendedor":
        return HttpResponseForbidden("No tienes permiso para acceder aquí.")

    compania = getattr(request.user, "compania", None)

    return render(
        request,
        "cuentas/vendedor_dashboard.html",
        {"compania": compania}
    )

@login_required
def inventario_nuevo(request):
    empresa = request.user.compania

    productos = Producto.objects.filter(compania=empresa, activo=True)
    sucursales = Sucursal.objects.filter(compania=empresa)

    if request.method == "POST":
        producto_id = request.POST.get("producto")
        sucursal_id = request.POST.get("sucursal")
        stock = int(request.POST.get("stock"))
        reposicion = int(request.POST.get("reposicion"))

        producto = Producto.objects.get(id=producto_id)
        sucursal = Sucursal.objects.get(id=sucursal_id)

        inv, created = Inventario.objects.get_or_create(
            producto=producto,
            sucursal=sucursal,
            defaults={"stock": stock, "punto_reposicion": reposicion}
        )

        if not created:
            inv.stock = stock
            inv.punto_reposicion = reposicion
            inv.save()

        return redirect("admin_inventario_listar")

    return render(request, "inventario_nuevo.html", {
        "productos": productos,
        "sucursales": sucursales,
    })

