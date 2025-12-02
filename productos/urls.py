from django.urls import path
from . import views

urlpatterns = [
    path('admin/productos/', views.admin_productos_listar, name='admin_productos_listar'),
    path('admin/productos/crear/', views.admin_productos_crear, name='admin_productos_crear'),
]
