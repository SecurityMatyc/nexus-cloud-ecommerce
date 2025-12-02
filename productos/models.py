from django.db import models
from main.models import Compania


class Producto(models.Model):
    compania = models.ForeignKey(Compania, on_delete=models.CASCADE, related_name='productos')
    sku = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # precio de venta
    costo = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # precio de costo
    categoria = models.CharField(max_length=100, blank=True)
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sku} - {self.nombre}"

    class Meta:
        app_label = 'productos'
