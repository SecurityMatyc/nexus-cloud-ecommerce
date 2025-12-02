from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Venta
from django.http import JsonResponse
from productos.models import Producto
from inventario.models import Inventario, Sucursal
from .models import Venta, DetalleVenta
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.http import JsonResponse
from productos.models import Producto


@login_required
def reportes_gerente(request):
    if request.user.rol not in ("admin_cliente", "gerente"):
        return HttpResponseForbidden("No tienes permiso para ver reportes.")

    ventas = Venta.objects.all().order_by("-created_at")[:50]  # simple, para partir
    return render(request, "ventas/reportes_gerente.html", {"ventas": ventas})

@login_required
def pos_vendedor(request):
    if request.user.rol != "vendedor":
        return HttpResponseForbidden("No tienes permiso para acceder aquí.")

    return render(request, "ventas/pos_vendedor.html")


# 🔹 NUEVO: HISTORIAL DEL VENDEDOR (stub)
@login_required
def ventas_historial(request):
    if request.user.rol != "vendedor":
        return HttpResponseForbidden("No tienes permiso para acceder aquí.")

    ventas = Venta.objects.filter(usuario=request.user).order_by("-created_at")
    return render(request, "ventas/ventas_historial.html", {"ventas": ventas})


@login_required
def buscar_productos(request):
    if request.user.rol != "vendedor":
        return HttpResponseForbidden("No permitido")

    q = request.GET.get("q", "").strip()
    sucursal_id = request.GET.get("sucursal")

    if not sucursal_id:
        return JsonResponse({"error": "Selecciona una sucursal"}, status=400)

    inventario = Inventario.objects.filter(
        sucursal_id=sucursal_id,
        producto__nombre__icontains=q
    ).select_related("producto")[:20]

    data = []
    for inv in inventario:
        data.append({
            "id": inv.producto.id,
            "sku": inv.producto.sku,
            "nombre": inv.producto.nombre,
            "stock": inv.stock,
            "precio": float(inv.producto.precio),
        })

    return JsonResponse(data, safe=False)

@login_required
def pos_vendedor(request):
    if request.user.rol != "vendedor":
        return HttpResponseForbidden("No tienes permiso.")

    compania = request.user.compania
    sucursales = Sucursal.objects.filter(compania=compania)

    return render(request, "ventas/pos_vendedor.html", {
        "sucursales": sucursales
    })

@csrf_exempt
@login_required
def registrar_venta(request):
    if request.user.rol != "vendedor":
        return JsonResponse({"error": "No tienes permiso"}, status=403)

    body = json.loads(request.body)

    sucursal_id = body.get("sucursal")
    items = body.get("items", [])

    if not sucursal_id or not items:
        return JsonResponse({"error": "Datos incompletos"}, status=400)

    sucursal = Sucursal.objects.get(id=sucursal_id)

    venta = Venta.objects.create(
        compania=request.user.compania,
        sucursal=sucursal,
        usuario=request.user,
        total=0
    )

    total_final = 0

    for item in items:
        producto = Producto.objects.get(id=item["id"])
        cantidad = int(item["cantidad"])
        precio = float(producto.precio)
        subtotal = cantidad * precio

        # Descontar stock
        inv = Inventario.objects.get(producto=producto, sucursal=sucursal)
        if inv.stock < cantidad:
            return JsonResponse({"error": f"Stock insuficiente para {producto.nombre}"}, status=400)

        inv.stock -= cantidad
        inv.save()

        DetalleVenta.objects.create(
            venta=venta,
            producto=producto,
            cantidad=cantidad,
            precio_unitario=precio,
            subtotal=subtotal
        )

        total_final += subtotal

    venta.total = total_final
    venta.save()

    return JsonResponse({"success": True, "venta_id": venta.id})

def buscar_productos(request):
    q = request.GET.get("q", "").strip().lower()

    productos = Producto.objects.filter(nombre__icontains=q)[:10]

    data = [
        {"id": p.id, "nombre": p.nombre, "precio": float(p.precio)}
        for p in productos
    ]

    return JsonResponse({"results": data})
