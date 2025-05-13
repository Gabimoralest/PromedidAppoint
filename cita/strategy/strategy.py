from cita.models import Cita
from django.core.exceptions import ValidationError

class EstrategiaAgendamiento:
    def validar(self, fecha, hora):
        raise NotImplementedError()

class AgendamientoNormal(EstrategiaAgendamiento):
    def validar(self, fecha, hora):
        if Cita.objects.filter(fecha=fecha, hora=hora).exists():
            raise ValidationError("Ya hay una cita programada en ese horario.")

class AgendamientoSueroterapia(EstrategiaAgendamiento):
    def validar(self, fecha, hora):
        total = Cita.objects.filter(fecha=fecha, hora=hora).count()
        if total >= 3:
            raise ValidationError("Ya hay 3 citas programadas para sueroterapia en ese horario.")
    
def obtener_estrategia(paquete):
    if "sueroterapia" in paquete.lower():
         return AgendamientoSueroterapia()
    return AgendamientoNormal()