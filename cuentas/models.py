from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from main.models import Compania


# ===============================
#  MANAGER PERSONALIZADO
# ===============================
class UsuarioManager(BaseUserManager):

    def create_user(self, email, nombre, password=None, rol="cliente_final", **extra_fields):
        if not email:
            raise ValueError("El usuario debe tener un email")

        email = self.normalize_email(email)

        usuario = self.model(
            email=email,
            nombre=nombre,
            rol=rol,
            **extra_fields
        )

        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, email, nombre, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, nombre, password, rol="superadmin", **extra_fields)


# ===============================
#  MODELO USUARIO PERSONALIZADO
# ===============================

ROLES = [
    ('superadmin', 'Super Administrador'),
    ('admin_cliente', 'Admin Cliente'),
    ('gerente', 'Gerente'),
    ('vendedor', 'Vendedor'),
    ('cliente_final', 'Cliente Final'),
]

class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=150)  # 🔥 sin blank, sin default
    compania = models.ForeignKey(Compania, on_delete=models.SET_NULL, null=True, blank=True)
    rol = models.CharField(max_length=20, choices=ROLES, default='cliente_final')

    # Campos necesarios para Django Admin
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre']

    def __str__(self):
        return f"{self.nombre} ({self.email})"
