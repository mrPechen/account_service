from rest_framework.response import Response
from rest_framework.views import APIView

from api.services.factory import HeaderFactory


class CreateUserView(APIView):

    def post(self, request):
        header = request.headers.get('x-Device')
        data = request.data
        choose_serializer = HeaderFactory.serializer(header)
        serializer = choose_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=201)

