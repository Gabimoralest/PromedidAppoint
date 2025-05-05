from .usuario_handler import UsuarioHandler
from usuario.models import Usuario

class AsesorHandler(UsuarioHandler):
    def handle(self, data):
        if data.get('rol') == 'asesor':
            return Usuario.objects.create_user(**data)
        return super().handle(data)

class RecepcionistaHandler(UsuarioHandler):
    def handle(self, data):
        if data.get('rol') == 'recepcionista':
            return Usuario.objects.create_user(**data)
        return super().handle(data)

class AdministradorHandler(UsuarioHandler):
    def handle(self, data):
        if data.get('rol') == 'administrador':
            return Usuario.objects.create_user(**data)
        return super().handle(data)
