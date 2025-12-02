from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponse
from .models import Sucursal, Inventario


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
