from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer, ReadOnlyField
from rest_framework.views import APIView

from api.models import Account


class GetUserView(APIView):
    class OutputSerializer(ModelSerializer):
        user_id = ReadOnlyField(source='id')
        birth_date = ReadOnlyField(source='user.birth_date')
        passport_number = ReadOnlyField(source='user.passport_number')
        place_of_birth = ReadOnlyField(source='user.place_of_birth')
        registration_address = ReadOnlyField(source='user.registration_address')
        residential_address = ReadOnlyField(source='user.residential_address')

        class Meta:
            model = Account
            fields = ['user_id', 'first_name', 'last_name', 'patronymic',
                      'phone', 'email', 'birth_date', 'passport_number',
                      'place_of_birth', 'registration_address',
                      'residential_address']
            ref_name = "OutputSerializer for get user by id"

    def get(self, request, user_id: int):
        data = get_object_or_404(Account, id=user_id)
        serializer = self.OutputSerializer(data)
        return Response(serializer.data, status=200)
