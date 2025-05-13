from django.core.exceptions import ValidationError
from rest_framework import viewsets
from cita.models import Cita
from cita.api.serializer import CitaSerializer
from cita.api.permissions import EsAdminOAsesor
from cita.strategy.strategy import obtener_estrategia

class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer
    permission_classes = [EsAdminOAsesor]

    def perform_create(self, serializer):
        data = serializer.validated_data
        estrategia = obtener_estrategia(data['paquete'])

        estrategia.validar(data['fecha'], data['hora'])

        serializer.save(registrado_por=self.request.user)