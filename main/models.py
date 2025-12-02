from django.db import models

# ============================
#   PLANES DE SUSCRIPCIÓN 
# ============================

class PlanSuscripcion(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)
    precio = models.IntegerField()  # precio mensual en pesos
    limite_usuarios = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"
    
# ============================
#   TIENDAS / COMPAÑÍAS 
# ============================

class Compania(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    direccion = models.CharField(max_length=200, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    
    # plan contratado
    plan = models.ForeignKey(PlanSuscripcion, on_delete=models.SET_NULL, null=True)

    # ¿La tienda ya está aprobada por el superadmin?
    aprobada = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre



