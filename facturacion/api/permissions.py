from rest_framework.permissions import BasePermission

class EsRecepcionista(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            getattr(request.user, 'rol', None) in ['recepcionista', 'administrador']
        )

