from django.db import models

from apps.base.models import BaseModel


class City(BaseModel):

    code = models.CharField(max_length=5, blank=True, null=True)
    name = models.CharField(max_length=100)
    prefix = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        db_table = 'cities'
        ordering = ['name']

    def __str__(self):
        return self.name


class District(BaseModel):

    code = models.CharField(max_length=5, blank=True, null=True)
    name = models.CharField(max_length=100)
    prefix = models.CharField(max_length=5, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    class Meta:
        db_table = 'districts'
        ordering = ['name']

    def __str__(self):
        return self.name


class Color(BaseModel):

    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'colors'

    def __str__(self):
        return self.name


class Specie(BaseModel):

    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'species'

    def __str__(self):
        return self.name


class ProductType(BaseModel):

    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'product_types'

    def __str__(self):
        return self.name


class Unit(BaseModel):

    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'units'

    def __str__(self):
        return self.name