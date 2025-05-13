from rest_framework import serializers
from sedes.models import Sede

class SedeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sede
        fields = '__all__'
