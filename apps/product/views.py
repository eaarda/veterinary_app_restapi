from rest_framework import viewsets

from apps.base.views import BaseModelViewSet
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(BaseModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer