from django.shortcuts import render
from rest_framework import generics
from .models import Animal
from .serializers import AnimalSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


class Animal_Objects(generics.ListCreateAPIView):
    serializer_class = AnimalSerializer

    def get_queryset(self):
        queryset = Animal.objects.all()
        return queryset
