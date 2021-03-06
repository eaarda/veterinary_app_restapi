from ..models import Appointment
from ..serializers import AppointmentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class Appointments(APIView):
    def get(self, request, format=None):
        queryset = Appointment.objects.all()
        serializer = AppointmentSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
