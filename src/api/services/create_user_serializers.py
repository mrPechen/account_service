import re

from django.db import transaction
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer, DateField, CharField, EmailField

from api.models import User, Account


class MailHeaderSerializer(ModelSerializer):
    first_name = CharField(required=True)
    email = EmailField(required=True)

    class Meta:
        model = Account
        fields = ['first_name', 'email']

    def create(self, validated_data):
        check_unique = Account.objects.filter(email=validated_data.get('email')).exists()
        if check_unique:
            raise ValidationError("Email already exists")
        return Account.objects.create(**validated_data)


class MobileHeaderSerializer(ModelSerializer):
    phone = CharField(required=True)

    class Meta:
        model = Account
        fields = ['phone']

    def validate_phone(self, value):
        pattern = re.compile(r'^7\d{10}$')
        if not pattern.match(value):
            raise ValidationError('Phone number must be in the format 7XXXXXXXXXX')
        return value

    def create(self, validated_data):
        check_unique = Account.objects.filter(phone=validated_data.get('phone')).exists()
        if check_unique:
            raise ValidationError("Phone already exists")
        return Account.objects.create(**validated_data)


class WebHeaderSerializer(ModelSerializer):
    first_name = CharField(required=True)
    last_name = CharField(required=True)
    patronymic = CharField(required=True)
    phone = CharField(required=True)
    birth_date = DateField(required=True)
    passport_number = CharField(required=True)
    place_of_birth = CharField(required=True)
    registration_address = CharField(required=True)

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'patronymic',
                  'phone', 'birth_date', 'passport_number',
                  'place_of_birth', 'registration_address']

    def validate_passport_number(self, value):
        pattern = re.compile(r'^\d{4}\s\d{6}$')
        if not pattern.match(value):
            raise ValidationError('Passport number must be in the format XXXX XXXXXXX')
        return value

    def validate_phone(self, value):
        pattern = re.compile(r'^7\d{10}$')
        if not pattern.match(value):
            raise ValidationError('Phone number must be in the format 7XXXXXXXXXX')
        return value

    def create(self, validated_data):
        with transaction.atomic():
            check_unique = Account.objects.filter(phone=validated_data.get('phone')).exists()
            if check_unique:
                raise ValidationError("Phone already exists")
            account_fields = ['first_name', 'last_name', 'patronymic', 'phone']
            account_data = {field: validated_data.pop(field) for field in account_fields}
            account = Account.objects.create(**account_data)
            return User.objects.create(account=account, **validated_data)
