from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponse
from .models import Sucursal, Inventario
from productos.models import Producto
from main.models import Compania
from cuentas.models import Usuario


@login_required
def admin_sucursales_listar(request):
    if request.user.rol != 'admin_cliente':
        return HttpResponseForbidden("No tienes permiso.")
    
    compania = request.user.compania
    if not compania:
        return HttpResponse("No hay compañía asignada.")
    
    sucursales = Sucursal.objects.filter(compania=compania)
    return render(request, "inventario/admin_sucursales_listar.html", {"sucursales": sucursales, "compania": compania})


@login_required
def admin_sucursales_crear(request):
    if request.user.rol != 'admin_cliente':
        return HttpResponseForbidden("No tienes permiso.")
    
    compania = request.user.compania
    if not compania:
        return HttpResponse("No hay compañía asignada.")
    
    if request.method == "POST":
        nombre = (request.POST.get("nombre") or "").strip()
        direccion = request.POST.get("direccion") or ""
        telefono = request.POST.get("telefono") or ""
        ciudad = request.POST.get("ciudad") or ""
        
        if not nombre:
            return render(request, "inventario/admin_sucursales_crear.html", 
                         {"error": "Ingresa nombre de sucursal.", "compania": compania})
        
        Sucursal.objects.create(
            compania=compania,
            nombre=nombre,
            direccion=direccion,
            telefono=telefono,
            ciudad=ciudad
        )
        return redirect("admin_sucursales_listar")
    
    return render(request, "inventario/admin_sucursales_crear.html", {"compania": compania})


@login_required
def admin_inventario_listar(request):
    if request.user.rol != 'admin_cliente':
        return HttpResponseForbidden("No tienes permiso.")
    
    compania = request.user.compania
    if not compania:
        return HttpResponse("No hay compañía asignada.")
    
    sucursal_id = request.GET.get("sucursal")
    sucursales = Sucursal.objects.filter(compania=compania)
    
    if sucursal_id:
        inventarios = Inventario.objects.filter(sucursal__compania=compania, sucursal_id=sucursal_id)
    else:
        inventarios = Inventario.objects.filter(sucursal__compania=compania)
    
    return render(request, "inventario/admin_inventario_listar.html", 
                 {"inventarios": inventarios, "sucursales": sucursales, "compania": compania})


@login_required
def listar_inventario(request):
    if request.user.rol not in ("admin_cliente", "gerente"):
        return HttpResponseForbidden("No tienes permiso para ver inventario.")

    inventario = Inventario.objects.select_related("producto", "sucursal")
    return render(request, "inventario/listar_inventario.html", {"inventario": inventario})


@login_required
def inventario_nuevo(request):
    empresa = request.user.compania

    productos = Producto.objects.filter(compania=empresa, activo=True)
    sucursales = Sucursal.objects.filter(compania=empresa)

    if request.method == "POST":
        producto_id = request.POST.get("producto")
        sucursal_id = request.POST.get("sucursal")
        stock = request.POST.get("stock")
        reposicion = request.POST.get("reposicion")

        producto = Producto.objects.get(id=producto_id)
        sucursal = Sucursal.objects.get(id=sucursal_id)

        inv, created = Inventario.objects.get_or_create(
            producto=producto,
            sucursal=sucursal,
            defaults={
                "stock": int(stock),
                "punto_reposicion": int(reposicion)
            }
        )

        if not created:
            inv.stock = int(stock)
            inv.punto_reposicion = int(reposicion)
            inv.save()

        return redirect("admin_inventario_listar")

    return render(request, "inventario_nuevo.html", {
        "productos": productos,
        "sucursales": sucursales
    })

