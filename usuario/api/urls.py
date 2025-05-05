from django.urls import path
from usuario.api.views import RegistrarUsuarioView, DetalleUsuarioView, ListaUsuariosView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('usuarios/registrar', RegistrarUsuarioView.as_view()),
    path('usuarios/listar', ListaUsuariosView.as_view()),
    path('usuarios/<int:id>', DetalleUsuarioView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
