from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer
from .models import Animal, Cat, Dog, Cow, Appointment


class AnimalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Animal
        fields = '__all__'


class CatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cat
        fields = '__all__'


class DogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dog
        fields = '__all__'


class CowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cow
        fields = '__all__'


class ProjectPolymorphicSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        Animal: AnimalSerializer,
        Cat: CatSerializer,
        Dog: DogSerializer,
        Cow: CowSerializer
    }


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'
