from rest_framework import serializers
from persona.models import Paciente, PersonalSalud

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

class PersonalSaludSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalSalud
        fields = '__all__'
