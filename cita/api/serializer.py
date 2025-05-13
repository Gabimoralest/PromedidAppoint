from rest_framework import serializers
from cita.models import Cita

class CitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cita
        fields = ['id', 'fecha', 'hora', 'estado', 'motivo', 'paquete', 'costo', 'paciente', 'doctor', 'registrado_por', 'sede']
