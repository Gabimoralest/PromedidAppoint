from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from usuario.models import Usuario
from usuario.api.serializers import UsuarioRegistroSerializer
from usuario.api.permissions import EsAdministrador
from rest_framework.permissions import IsAuthenticated
from usuario.handlers.handlers_roles import AsesorHandler, RecepcionistaHandler, AdministradorHandler

class RegistrarUsuarioView(APIView):
    
    def post(self, request):
        serializer = UsuarioRegistroSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.validated_data
            
            asesor = AsesorHandler()
            recepcionista = RecepcionistaHandler()
            administrador = AdministradorHandler()

            asesor.set_next(recepcionista).set_next(administrador)

            try:
                usuario = asesor.handle(data)
                return Response({"mensaje": "Usuario creado correctamente."}, status=status.HTTP_201_CREATED)
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ListaUsuariosView(APIView):
    permission_classes = [IsAuthenticated, EsAdministrador]

    def get(self, request):
        usuarios = Usuario.objects.all()
        serializer = UsuarioRegistroSerializer(usuarios, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class DetalleUsuarioView(APIView):
    permission_classes = [IsAuthenticated, EsAdministrador]

    def get(self, request, id):
        try:
            usuario = Usuario.objects.get(pk=id)
            serializer = UsuarioRegistroSerializer(usuario)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Usuario.DoesNotExist:
            return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        
        try:
            usuario = Usuario.objects.get(pk=id)
        except Usuario.DoesNotExist:
            return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UsuarioRegistroSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mensaje': 'Usuario actualizado correctamente'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            usuario = Usuario.objects.get(pk=id)
            usuario.delete()
            return Response({'mensaje': 'Usuario eliminado correctamente'}, status=status.HTTP_204_NO_CONTENT)
        except Usuario.DoesNotExist:
            return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)
