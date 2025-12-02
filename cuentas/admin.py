from django.contrib import admin
from .models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('email', 'nombre', 'rol', 'is_active')
    list_filter = ('rol', 'is_active')
    search_fields = ('email', 'nombre')
    ordering = ('email',)

admin.site.register(Usuario, UsuarioAdmin)
