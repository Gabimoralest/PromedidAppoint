class Handler:
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    def handle(self, request, data):
        if self._next_handler:
            return self._next_handler.handle(request, data)
        raise PermissionError("No tienes permisos para realizar esta acción.")
