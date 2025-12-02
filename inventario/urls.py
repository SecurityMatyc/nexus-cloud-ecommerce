from django.urls import path
from . import views

urlpatterns = [
    path('admin/sucursales/', views.admin_sucursales_listar, name='admin_sucursales_listar'),
    path('admin/sucursales/crear/', views.admin_sucursales_crear, name='admin_sucursales_crear'),
    path('admin/inventario/', views.admin_inventario_listar, name='admin_inventario_listar'),
    path("inventario/", views.listar_inventario, name="listar_inventario"),
]