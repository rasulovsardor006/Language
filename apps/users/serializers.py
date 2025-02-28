from rest_framework import serializers
import validate
from phonenumber_field.phonenumber import PhoneNumber


class PhoneNumberSerializer(serializers.Serializer):
    phone = serializers.CharField(validate=[PhoneNumber])