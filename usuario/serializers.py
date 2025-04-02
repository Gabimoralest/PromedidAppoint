from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    
    id_usuario = serializers.IntegerField(source='id', read_only=True)
    nombre_usuario = serializers.CharField(source='username')
    correo = serializers.EmailField(source='email')
    rol_usuario = serializers.CharField(source='rol')
    
    class Meta:
        model = Usuario
        fields = ['id_usuario', 'nombre_usuario', 'correo', 'rol_usuario']