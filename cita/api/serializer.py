from rest_framework import serializers
from cita.models import Cita

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
