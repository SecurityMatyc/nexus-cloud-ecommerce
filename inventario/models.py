from django.db import models
from productos.models import Producto


class Sucursal(models.Model):
    compania = models.ForeignKey('main.Compania', on_delete=models.CASCADE, related_name='sucursales')
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    ciudad = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} ({self.compania.nombre})"

    class Meta:
        app_label = 'inventario'


class Inventario(models.Model):
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name='inventarios')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='inventarios')
    stock = models.IntegerField(default=0)
    punto_reorden = models.IntegerField(default=10)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('sucursal', 'producto')
        app_label = 'inventario'

    def __str__(self):
        return f"{self.producto.nombre} - {self.sucursal.nombre} ({self.stock})"
