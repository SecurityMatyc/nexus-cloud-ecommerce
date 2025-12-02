from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponse
from .models import Producto


@login_required
def admin_productos_listar(request):
    if request.user.rol != 'admin_cliente':
        return HttpResponseForbidden("No tienes permiso.")
    
    compania = request.user.compania
    if not compania:
        return HttpResponse("No hay compañía asignada.")
    
    productos = Producto.objects.filter(compania=compania)
    return render(request, "productos/admin_productos_listar.html", {"productos": productos, "compania": compania})


@login_required
def admin_productos_crear(request):
    if request.user.rol != 'admin_cliente':
        return HttpResponseForbidden("No tienes permiso.")
    
    compania = request.user.compania
    if not compania:
        return HttpResponse("No hay compañía asignada.")
    
    if request.method == "POST":
        sku = (request.POST.get("sku") or "").strip()
        nombre = (request.POST.get("nombre") or "").strip()
        descripcion = request.POST.get("descripcion") or ""
        precio = request.POST.get("precio") or "0"
        costo = request.POST.get("costo") or "0"
        categoria = request.POST.get("categoria") or ""
        
        if not sku or not nombre or not precio:
            return render(request, "productos/admin_productos_crear.html", 
                         {"error": "Rellena sku, nombre y precio.", "compania": compania})
        
        if Producto.objects.filter(sku=sku).exists():
            return render(request, "productos/admin_productos_crear.html", 
                         {"error": "SKU ya existe.", "compania": compania})
        
        Producto.objects.create(
            compania=compania,
            sku=sku,
            nombre=nombre,
            descripcion=descripcion,
            precio=float(precio),
            costo=float(costo),
            categoria=categoria
        )
        return redirect("admin_productos_listar")
    
    return render(request, "productos/admin_productos_crear.html", {"compania": compania})

@login_required
def listar_productos(request):
    # Solo admin_cliente, gerente o vendedor
    if request.user.rol not in ("admin_cliente", "gerente", "vendedor"):
        return HttpResponseForbidden("No tienes permiso para ver productos.")

    productos = Producto.objects.all()
    return render(request, "productos/listar_productos.html", {"productos": productos})