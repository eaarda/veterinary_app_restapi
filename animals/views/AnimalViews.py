from ..models import Animal
from ..serializers import ProjectPolymorphicSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class Animal_Objects(APIView):

    def get(self, request, format=None):
        queryset = Animal.objects.all()
        serializer = ProjectPolymorphicSerializer(queryset, many=True)
        return Response(serializer.data)


class Animal_Detail(APIView):

    def get(self, request, pk, format=None):
        animal = Animal.objects.get(pk=pk)
        serializer = ProjectPolymorphicSerializer(animal)
        return Response(serializer.data)
