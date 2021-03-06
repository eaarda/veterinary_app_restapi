from ..models import Cow
from ..serializers import CowSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class Cow_Objects(APIView):
    def get(self, request, format=None):
        queryset = Cow.objects.all()
        serializer = CowSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CowSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Cow_Detail(APIView):
    def get(self, request, pk, format=None):
        cow = Cow.objects.get(pk=pk)
        serializer = CowSerializer(cow)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        cow = Cow.objects.get(pk=pk)
        serializer = CowSerializer(cow, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, foramt=None):
        cow = Cow.objects.get(pk=pk)
        cow.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
