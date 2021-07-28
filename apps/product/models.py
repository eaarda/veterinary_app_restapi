from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.base.models import BaseModel
from apps.user.models import CustomUser
from apps.common.models import ProductType, Unit


class Product(BaseModel):

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE)

    barcode = models.CharField(max_length=20)
    code = models.CharField(max_length=20)
    
    sales_price = models.DecimalField(max_digits=9, decimal_places=2)
    purchase_price = models.DecimalField(max_digits=9, decimal_places=2)
    stock = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'products'
    
    def __str__(self):
        return self.name