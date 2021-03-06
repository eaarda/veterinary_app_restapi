from ..models import Animal
from ..serializers import AnimalSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class Animal_Objects(APIView):

    def get(self, request, format=None):
        queryset = Animal.objects.all()
        serializer = AnimalSerializer(queryset, many=True)
        return Response(serializer.data)
