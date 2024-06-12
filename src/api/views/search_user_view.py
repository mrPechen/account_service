from rest_framework.fields import ReadOnlyField
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.views import APIView

from api.models import Account
from api.services.filter_srvices import FilterService


class SearchUserView(APIView):
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
            ref_name = "OutputSerializer for search user"

    def get(self, request):
        query_params = request.query_params
        if query_params:
            query = {key: query_params.get(key) for key in query_params.keys()}
            data = FilterService.search_users(**query)
            serializer = self.OutputSerializer(data, many=True)
            return Response(serializer.data, status=200)
        return Response(status=404)
