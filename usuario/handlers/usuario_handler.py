class UsuarioHandler:
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    def handle(self, data):
        if self._next_handler:
            return self._next_handler.handle(data)
        raise ValueError("No se encontró ningún controlador para este rol.")
