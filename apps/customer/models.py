from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.base.models import BaseModel
from apps.user.models import CustomUser
from apps.common.models import City, District

class AnimalKind(models.TextChoices):
    CAT = 'cat', _('Kedi')
    DOG = 'dog', _('Dog')
    EXOTIC = 'exotic', _('Egzotik')
    WINGED = 'winged', _('Kanatlı')
    TROPICAL = 'tropical', _('Tropikal')
    WILD = 'wild', _('Yabani')
    OTHER = 'other', _('Dİğer')

class AnimalGender(models.TextChoices):
    MALE = 'male',_('Erkek')
    FEMALE = 'female', _('Dişi')


class Customer(BaseModel):

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="customers")

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)

    email = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    tax_vkn_number = models.CharField(max_length=20, blank=True, null=True)
    tax_office = models.CharField(max_length=255, blank=True, null=True)

    address = models.CharField(max_length=255, blank=True, null=True)
    district = models.ForeignKey(District, on_delete=models.PROTECT)
    city = models.ForeignKey(City, on_delete=models.PROTECT)

    class Meta:
        db_table = 'customers'
    
    def __str__(self):
        return f" {self.first_name} {self.last_name}"


class Animal(BaseModel):

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
    passport = models.CharField(max_length=100)
    birthday = models.DateField(auto_now=False, blank=True, null=True)
    kind = models.CharField(max_length=20, choices=AnimalKind.choices, default=AnimalKind.OTHER)
    spayed = models.BooleanField(default=False, blank=True, null=True, help_text='kısırlaştırılmış')
    specie = models.CharField(max_length=255, blank=True, null=True, help_text='ırk/tür')
    color = models.CharField(max_length=255, blank=True, null=True) 
    gender = models.CharField(max_length=20, choices=AnimalGender.choices, default=AnimalGender.FEMALE)

    owner = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True, related_name='animals')

    class Meta:
        db_table = 'animals'
    
    def __str__(self):
        return self.name


class Appointment(BaseModel):

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='appointments')
    day = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)

    description = models.TextField(blank=True, null=True)


    class Meta:
        db_table = 'appointments'
    
    def __str__(self):
        return f"{self.animal.name} - {self.day}"