from django.urls import path
from persona.api.views import RegistrarPersonaView, ListarPersonasView, DetallePersonaView

urlpatterns = [
    path('registrar/', RegistrarPersonaView.as_view()),
    path('listar/', ListarPersonasView.as_view()),
    path('<int:id>/', DetallePersonaView.as_view()),
]

