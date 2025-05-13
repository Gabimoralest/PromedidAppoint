from django.db import models
from persona.models import Paciente, PersonalSalud
from usuario.models import Usuario
from sedes.models import Sede


class Cita(models.Model):
    
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
        ('completada', 'Completada'),
    ]
    
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=15, choices=ESTADOS, default='pendiente')
    motivo = models.TextField()
    paquete = models.CharField(max_length=100)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    doctor = models.ForeignKey(PersonalSalud, on_delete=models.PROTECT)
    sede = models.ForeignKey(Sede, on_delete=models.PROTECT)
    registrado_por = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    
    def _str_(self):
        return f"Cita {self.id} - {self.paciente.nombre} - {self.estado}"
