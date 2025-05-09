from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from persona.api.serializers import PacienteSerializer, PersonalSaludSerializer
from persona.models import Paciente, PersonalSalud
from persona.handlers.handlers_roles import AdminHandler, AsesorHandler
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

class RegistrarPersonaView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        serializer_class = (
            PersonalSaludSerializer if 'especialidad' in data else PacienteSerializer
        )
        serializer = serializer_class(data=data)
        if serializer.is_valid():
            admin = AdminHandler()
            asesor = AsesorHandler()
            admin.set_next(asesor)
            try:
                persona = admin.handle(request, serializer.validated_data)
                return Response(serializer_class(persona).data, status=status.HTTP_201_CREATED)
            except PermissionError as e:
                return Response({'detail': str(e)}, status=status.HTTP_403_FORBIDDEN)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListarPersonasView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        pacientes = Paciente.objects.all()
        doctores = PersonalSalud.objects.all()

        pacientes_serializados = PacienteSerializer(pacientes, many=True).data
        doctores_serializados = PersonalSaludSerializer(doctores, many=True).data

        return Response({
            'pacientes': pacientes_serializados,
            'personal_salud': doctores_serializados
        })


class DetallePersonaView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, id):
        return (
            get_object_or_404(PersonalSalud, pk=id)
            if PersonalSalud.objects.filter(pk=id).exists()
            else get_object_or_404(Paciente, pk=id)
        )

    def get(self, request, id):
        persona = self.get_object(id)
        serializer_class = (
            PersonalSaludSerializer if isinstance(persona, PersonalSalud) else PacienteSerializer
        )
        serializer = serializer_class(persona)
        return Response(serializer.data)

    def put(self, request, id):
        persona = self.get_object(id)
        serializer_class = (
            PersonalSaludSerializer if isinstance(persona, PersonalSalud) else PacienteSerializer
        )
        serializer = serializer_class(persona, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'mensaje': 'Persona actualizada correctamente'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            persona = self.get_object(id)
            persona.desactivar()
            return Response({'mensaje': 'Persona desactivada correctamente'}, status=status.HTTP_200_OK)
        except persona.DoesNotExist:
            return Response({'error': 'Persona no encontrada'}, status=status.HTTP_404_NOT_FOUND)
