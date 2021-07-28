from django.db.models import fields
from rest_framework import serializers

from .models import City, District, Color, Specie, ProductType, Unit


class CitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = City
        fields = ('id', 'name')


class DistrictSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = District
        fields = ('id', 'name', 'city')


class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = ('id', 'name')


class SpecieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Specie
        fields = ('id', 'name')


class ProductTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductType
        fields = ('id', 'name')


class UnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Unit
        fields = ('id', 'name')