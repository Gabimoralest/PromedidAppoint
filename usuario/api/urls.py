from django.urls import path
from usuario.api.views import RegistrarUsuarioView, DetalleUsuarioView

urlpatterns = [
    path('usuarios/', RegistrarUsuarioView.as_view()),
    path('usuarios/<int:id>', DetalleUsuarioView.as_view()),
]
