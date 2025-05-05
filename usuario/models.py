from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.

class Usuario(AbstractUser):
    ROLES = [
        ('administrador', 'Administrador'),
        ('recepcionista', 'Recepcionista'),
        ('asesor', 'Asesor')
    ]
    
    grupos = models.ManyToManyField(
        Group,
        related_name="usuario_grupos",  
        blank=True
    )
    
    usuario_permisos = models.ManyToManyField(
        Permission,
        related_name="usuario_permisos",  
        blank=True
    )
    
    rol = models.CharField(max_length=20, choices=ROLES)
    email = models.EmailField(blank=True, null=True)
    
    def __str__(self):
        return f'Usuario: {self.username} - Rol: {self.get_rol_display()}'
