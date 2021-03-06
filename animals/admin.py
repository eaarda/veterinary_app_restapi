from django.contrib import admin
from .models import Animal, Cat, Dog, Cow, Appointment
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, PolymorphicChildModelFilter


# Register your models here.
admin.site.register(Appointment)


@admin.register(Animal)
class AnimalAdmin(PolymorphicParentModelAdmin):
    base_model = Animal
    child_models = (Cat, Dog, Cow)
    list_filter = (PolymorphicChildModelFilter,)  # optional.


@admin.register(Cat)
class CatAdmin(PolymorphicChildModelAdmin):
    base_model = Cat


@admin.register(Dog)
class DogAdmin(PolymorphicChildModelAdmin):
    base_model = Dog


@admin.register(Cow)
class CowAdmin(PolymorphicChildModelAdmin):
    base_model = Cow
