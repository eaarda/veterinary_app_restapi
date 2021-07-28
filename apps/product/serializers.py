from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            'id', 
            'name',
            'unit',
            'type',
            'barcode',
            'code',
            'sales_price',
            'purchase_price',
            'stock' )