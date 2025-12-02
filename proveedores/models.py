from django.db import models
from main.models import Compania


class Proveedor(models.Model):
    compania = models.ForeignKey(Compania, on_delete=models.CASCADE, related_name='proveedores')
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12)
    contacto = models.CharField(max_length=100, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    direccion = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} ({self.compania.nombre})"

    class Meta:
        app_label = 'proveedores'
