from django.urls import path
from .views import user_login, user_logout
from . import views


urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('dashboard/', views.dashboard_redirect, name='dashboard_redirect'),
    path('superadmin/', views.dashboard_superadmin, name='dashboard_superadmin'),
    path('admin_cliente/', views.dashboard_admin_cliente, name='dashboard_admin_cliente'),
    path("companias/", views.companias_listar, name="compania_listar"),
    path("companias/crear/", views.compania_crear, name="compania_crear"),
    path("usuarios/", views.usuarios_listar, name="usuario_listar"),
    path("usuarios/crear/", views.usuario_crear, name="usuario_crear"),
    
    # Admin Cliente — Usuarios
    path("admin/usuarios/", views.admin_usuarios_listar, name="admin_usuarios_listar"),
    path("admin/usuarios/crear/", views.admin_usuarios_crear, name="admin_usuarios_crear"),
]
