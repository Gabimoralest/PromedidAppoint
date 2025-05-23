from django.db import models
from sedes.models import Sede

class Persona(models.Model):
    
    TIPO_IDENTIFICACION = [
        ('CC', 'Cédula de Ciudadanía'),
        ('TI', 'Tarjeta de Identidad'),
        ('CE', 'Cédula de Extranjería'),
    ]

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    tipo_identificacion = models.CharField(max_length=2, choices=TIPO_IDENTIFICACION)
    documento = models.CharField(max_length=20, unique=True)
    correo = models.EmailField(unique=True)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=15)
    estado = models.CharField(max_length=50,default='Activo')
    
    def desactivar(self):
        self.estado = 'Inactivo'
        self.save()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Paciente(Persona):
    pass

class PersonalSalud(Persona):
    especialidad = models.CharField(max_length=100)
    sede = models.ForeignKey(Sede, on_delete=models.PROTECT, null=True, blank=True)

