from django.urls import path
from persona.api.views import RegistrarPersonaView, ListarPersonasView, DetallePersonaView

urlpatterns = [
    path('personas/registrar/', RegistrarPersonaView.as_view()),
    path('personas/listar', ListarPersonasView.as_view()),
    path('personas/<int:id>', DetallePersonaView.as_view()),
]

