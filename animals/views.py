from django.shortcuts import render
from .models import Animal, Cat
from .serializers import AnimalSerializer, CatSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class Animal_Objects(APIView):

    def get(self, request, format=None):
        queryset = Animal.objects.all()
        serializer = AnimalSerializer(queryset, many=True)
        return Response(serializer.data)


class Cat_Objects(APIView):
    def get(self, request, format=None):
        queryset = Cat.objects.all()
        serializer = CatSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
