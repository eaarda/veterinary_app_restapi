from rest_framework import viewsets

from .models import City, District, Color, Specie, ProductType, Unit
from .serializers import CitySerializer, DistrictSerializer, ColorSerializer, SpecieSerializer, ProductTypeSerializer, UnitSerializer


class CityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class DistrictViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer


class ColorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class SpecieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Specie.objects.all()
    serializer_class = SpecieSerializer


class ProductTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer


class UnitViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer