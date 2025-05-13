from django.db import models
from cita.models import Cita 

class Factura(models.Model):
    idfactura = models.AutoField(primary_key=True)
    fechafactura = models.DateField(auto_now_add=True)
    formapago = models.CharField(max_length=50)
    montototal = models.DecimalField(max_digits=10, decimal_places=2)
    descuento = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    idcita = models.ForeignKey(Cita, on_delete=models.CASCADE, related_name='facturas')

    def _str_(self):
        return f"Factura {self.idfactura} - Cita {self.idcita.id}"