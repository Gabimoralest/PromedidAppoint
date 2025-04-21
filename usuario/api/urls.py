from django.urls import path
from usuario.api.views import RegistrarUsuarioView

urlpatterns = [
    path('usuarios/', RegistrarUsuarioView.as_view()),
]
