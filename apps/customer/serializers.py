from rest_framework import serializers

from apps.customer.models import Customer, Animal, Appointment
from apps.common.serializers import CitySerializer, DistrictSerializer


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = (
            'id', 
            'first_name', 
            'last_name', 
            'phone', 
            'email', 
            'description',
            'tax_vkn_number',
            'tax_office',
            'address',
            'district',
            'city' )
    
    def to_representation(self, instance):
        self.fields["city"] = CitySerializer(allow_null=True)
        self.fields["district"] = DistrictSerializer(allow_null=True)
        return super(CustomerSerializer, self).to_representation(instance)


class AnimalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Animal
        fields = (
            'id',
            'name',
            'passport',
            'birthday',
            'kind',
            'spayed',
            'specie',
            'color',
            'gender',
            'owner'
        )


class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = (
            'id',
            'created_at',
            'active',
            'day',
            'time',
            'description',
            'animal'
        )