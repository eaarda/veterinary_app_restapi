from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.base.views import BaseModelViewSet
from .models import Customer, Animal, Appointment
from .serializers import CustomerSerializer, AnimalSerializer, AppointmentSerializer


class CustomerViewSet(BaseModelViewSet):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    @action(detail=True, methods=['GET'], url_path='animals', url_name='animals')
    def animals(self, request, *args, **kwargs):
        obj = self.get_object()
        return Response(AnimalSerializer(obj.animals, many=True).data, status=status.HTTP_200_OK)

class AnimalViewSet(BaseModelViewSet):

    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

    @action(detail=True, methods=['GET'], url_path='appointments', url_name='appointments')
    def appointments(self, request, *args, **kwargs):
        obj = self.get_object()
        return Response(AppointmentSerializer(obj.appointments, many=True).data, status=status.HTTP_200_OK)


class AppointmentViewSet(BaseModelViewSet):

    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer