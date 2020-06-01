from rest_framework.response import Response
from rest_framework.views import APIView

from ..entidades import tecnologia
from ..services import tecnologia_services
from ..serializers import tecnologia_serializer
from rest_framework import status


class TecnologiaList(APIView):
    def get(self, request, format=None):
        tecnologias = tecnologia_services.listar_tecnologias()
        serializer = tecnologia_serializer.TecnologiaSerializer(tecnologias, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = tecnologia_serializer.TecnologiaSerializer(data=request.data)
        if serializer.is_valid():
            nome = serializer.validated_data["nome"]
            tecnologia_nova = tecnologia.Tecnologia(nome=nome)
            tecnologia_bd = tecnologia_services.cadastrar_tecnologia(tecnologia_nova)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TecnolgiaDetalhes(APIView):
    def get(self, request, id, format=None):
        tecnologia = tecnologia_services.listar_tecnologia_id(id)
        serializer = tecnologia_serializer.TecnologiaSerializer(tecnologia)
        return Response(serializer.data, status=status.HTTP_200_OK)