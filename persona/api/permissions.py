from rest_framework.permissions import BasePermission

class EsAdminOAsesor(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.rol in ['administrador', 'asesor']

class SoloAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.rol == 'administrador'
