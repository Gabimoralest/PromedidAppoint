from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from usuario.models import Usuario
from usuario.api.serializers import UsuarioRegistroSerializer
from usuario.api.permissions import EsAdministrador
from rest_framework.permissions import IsAuthenticated

class RegistrarUsuarioView(APIView):
    permission_classes = [IsAuthenticated, EsAdministrador]

    def post(self, request):
        serializer = UsuarioRegistroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mensaje': 'Usuario registrado correctamente'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
