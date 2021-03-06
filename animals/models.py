from django.db import models
from polymorphic.models import PolymorphicModel


class Animal(PolymorphicModel):
    name = models.CharField(max_length=80)
    birthday = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)


class Cat(Animal):
    owner_name = models.CharField(max_length=80)

    def __str__(self):
        return str(self.name)


class Dog(Animal):
    owner_name = models.CharField(max_length=80)

    def __str__(self):
        return str(self.name)


class Cow(Animal):
    farm_name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)


class Appointment(models.Model):
    animal_id = models.ForeignKey(
        Animal, related_name='animals', on_delete=models.CASCADE)
    appointment_datetime = models.DateTimeField(null=True)
    description = models.CharField(max_length=500, null=True)

    def __str__(self):
        return str(self.animal_id)
