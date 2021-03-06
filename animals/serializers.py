from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer
from .models import Animal, Cat, Dog, Cow, Appointment


class AnimalSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    birthday = serializers.CharField()
    updated_at = serializers.CharField()

    class Meta:
        model = Animal
        fields = '__all__'


class CatSerializer(serializers.ModelSerializer):
    owner_name = serializers.CharField()

    class Meta:
        model = Cat
        fields = '__all__'


class DogSerializer(serializers.ModelSerializer):
    owner_name = serializers.CharField()

    class Meta:
        model = Dog
        fields = '__all__'


class CowSerializer(serializers.ModelSerializer):
    farm_name = serializers.CharField()

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
