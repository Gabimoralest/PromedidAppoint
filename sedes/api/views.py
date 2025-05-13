# sede/views.py
from rest_framework import viewsets
from sedes.models import Sede
from sedes.api.serializer import SedeSerializer

class SedeViewSet(viewsets.ModelViewSet):
    queryset = Sede.objects.all()
    serializer_class = SedeSerializer

