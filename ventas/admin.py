from django.contrib import admin
from .models import Venta

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ("id", "compania", "sucursal", "usuario", "total", "created_at")
    list_filter = ("compania", "sucursal", "usuario")
    search_fields = ("id", "usuario__nombre")

