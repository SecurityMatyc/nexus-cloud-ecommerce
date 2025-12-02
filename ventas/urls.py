from django.urls import path
from . import views

urlpatterns = [
    path("reportes/gerente/", views.reportes_gerente, name="reportes_gerente"),
    path("vendedor/pos/", views.pos_vendedor, name="pos_vendedor"),
    path("vendedor/ventas/", views.ventas_historial, name="ventas_historial"),
    path("vendedor/pos/buscar-productos/", views.buscar_productos, name="buscar_productos"),
    path("vendedor/pos/registrar/", views.registrar_venta, name="registrar_venta"),
    path("buscar/", views.buscar_productos, name="buscar_productos"),

]
