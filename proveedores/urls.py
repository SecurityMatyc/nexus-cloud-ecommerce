from django.urls import path
from . import views

urlpatterns = [
    path('admin/proveedores/', views.admin_proveedores_listar, name='admin_proveedores_listar'),
    path('admin/proveedores/crear/', views.admin_proveedores_crear, name='admin_proveedores_crear'),
]
