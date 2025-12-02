from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponse
from .models import Proveedor


@login_required
def admin_proveedores_listar(request):
    if request.user.rol != 'admin_cliente':
        return HttpResponseForbidden("No tienes permiso.")
    
    compania = request.user.compania
    if not compania:
        return HttpResponse("No hay compañía asignada.")
    
    proveedores = Proveedor.objects.filter(compania=compania)
    return render(request, "proveedores/admin_proveedores_listar.html", {"proveedores": proveedores, "compania": compania})


@login_required
def admin_proveedores_crear(request):
    if request.user.rol != 'admin_cliente':
        return HttpResponseForbidden("No tienes permiso.")
    
    compania = request.user.compania
    if not compania:
        return HttpResponse("No hay compañía asignada.")
    
    if request.method == "POST":
        nombre = (request.POST.get("nombre") or "").strip()
        rut = (request.POST.get("rut") or "").strip()
        contacto = request.POST.get("contacto") or ""
        telefono = request.POST.get("telefono") or ""
        email = request.POST.get("email") or ""
        direccion = request.POST.get("direccion") or ""
        
        if not nombre or not rut:
            return render(request, "proveedores/admin_proveedores_crear.html", 
                         {"error": "Ingresa nombre y RUT.", "compania": compania})
        
        Proveedor.objects.create(
            compania=compania,
            nombre=nombre,
            rut=rut,
            contacto=contacto,
            telefono=telefono,
            email=email,
            direccion=direccion
        )
        return redirect("admin_proveedores_listar")
    
    return render(request, "proveedores/admin_proveedores_crear.html", {"compania": compania})
