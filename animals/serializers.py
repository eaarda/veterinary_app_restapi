from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer
from .models import Animal


class AnimalSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    birthday = serializers.CharField()
    updated_at = serializers.CharField()

    class Meta:
        model = Animal
        fields = '__all__'


class AnimalPolymorphicSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        Animal: AnimalSerializer
    }
