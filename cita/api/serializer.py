from rest_framework import serializers
from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework.exceptions import ValidationError as DRFValidationError
from cita.models import Cita
from cita.strategy.strategy import obtener_estrategia

class CitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cita
        fields = ['id', 'fecha', 'hora', 'estado', 'motivo', 'paquete', 'costo', 'paciente', 'doctor', 'registrado_por', 'sede']
        
    def validate(self, data):
        hora_cita = data.get('hora')
        sede = data.get('sede')

        if sede and hora_cita:
            if sede.hora_inicio_atencion and sede.hora_fin_atencion:
                if not (sede.hora_inicio_atencion <= hora_cita <= sede.hora_fin_atencion):
                    raise serializers.ValidationError({
                        'hora': f"La hora de la cita ({hora_cita}) está fuera del horario de atención de la sede: {sede.hora_inicio_atencion} - {sede.hora_fin_atencion}."
                    })

        return data
    
    def validate(self, data):
        fecha = data.get('fecha')
        hora = data.get('hora')
        paquete = data.get('paquete', '')

        estrategia = obtener_estrategia(paquete)
        try:
            estrategia.validar(fecha, hora)
        except DjangoValidationError as e:
            raise DRFValidationError({"detalle": e.message})
        
        return data
