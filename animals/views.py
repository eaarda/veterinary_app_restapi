from django.shortcuts import render
from .models import Animal
from .serializers import AnimalSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class Animal_Objects(APIView):

    def get(self, request, format=None):
        queryset = Animal.objects.all()
        serializer_class = AnimalSerializer(queryset, many=True)
        return Response(serializer_class.data)
