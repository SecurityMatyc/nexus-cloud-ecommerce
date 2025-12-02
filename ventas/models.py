from django.db import models
from cuentas.models import Usuario
from inventario.models import Sucursal
from main.models import Compania
from django.conf import settings
from productos.models import Producto


class Venta(models.Model):
    compania = models.ForeignKey(
        Compania,
        on_delete=models.CASCADE,
        related_name="ventas"
    )

    sucursal = models.ForeignKey(
        Sucursal,
        on_delete=models.CASCADE,
        related_name="ventas"
    )

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.SET_NULL,
        null=True,
        related_name="ventas"
    )

    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    # Opcional: detalle de productos vendidos
    detalle = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"Venta {self.id} - {self.compania.nombre} - ${self.total}"



class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name="detalles")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.producto.nombre} x{self.cantidad}"


