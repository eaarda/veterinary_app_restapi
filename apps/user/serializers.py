
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions as django_exceptions
from django.db import IntegrityError, transaction
from django.db.models import fields

from rest_framework import serializers
from rest_framework.settings import api_settings

from .models import CustomUser


class UserCreateSerializer(serializers.ModelSerializer):

    password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    title = serializers.CharField()
    name = serializers.CharField()
    phone = serializers.CharField()


    class Meta:
        model = CustomUser
        fields = ('__all__')

    
    def validate(self, attrs):
        user = CustomUser(**attrs)
        password = attrs.get("password")

        try:
            validate_password(password, user)
        except django_exceptions.ValidationError as e:
            serializer_error = serializers.as_serializer_error(e)
            raise serializers.ValidationError(
                {"password": serializer_error[api_settings.NON_FIELD_ERRORS_KEY]}
            )

        return attrs
    
    def create(self, validated_data):
        try:
            user = self.perform_create(validated_data)
        except IntegrityError:
            self.fail("cannot_create_user")

        return user
    
    def perform_create(self, validated_data):
        with transaction.atomic():
            user = CustomUser.objects.create_user(**validated_data)
        return user


class UserProfileSerializer(serializers.ModelSerializer):

    email = serializers.CharField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'name', 'title', 'phone')