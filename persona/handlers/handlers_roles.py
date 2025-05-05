from .handlers import Handler
from persona.models import Paciente, PersonalSalud

class AdminHandler(Handler):
    def handle(self, request, data):
        if request.user.rol == 'administrador':
            if 'especialidad' in data:
                return PersonalSalud.objects.create(**data)
            else:
                return Paciente.objects.create(**data)
        return super().handle(request, data)

class AsesorHandler(Handler):
    def handle(self, request, data):
        if request.user.rol == 'asesor' and 'especialidad' not in data:
            return Paciente.objects.create(**data)
        return super().handle(request, data)

