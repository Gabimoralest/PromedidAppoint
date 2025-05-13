from rest_framework import viewsets
from facturacion.models import Factura
from facturacion.api.serializer import FacturaSerializer
from .permissions import EsRecepcionista
from rest_framework.permissions import IsAuthenticated

class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer
    permission_classes = [IsAuthenticated, EsRecepcionista]