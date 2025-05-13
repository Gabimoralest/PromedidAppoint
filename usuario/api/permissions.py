from rest_framework.permissions import BasePermission

class EsAdministrador(BasePermission):
    def has_permission(self, request, view): 
        return request.user.is_authenticated and request.user.rol == 'administrador'

class EsRecepcionista(BasePermission):
    def has_permission(self, request, view):  
        return request.user.is_authenticated and request.user.rol == 'recepcionista'

class EsAsesor(BasePermission):
    def has_permission(self, request, view):  
        return request.user.is_authenticated and request.user.rol == 'asesor'
