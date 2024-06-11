from api.services.create_user_serializers import MailHeaderSerializer, MobileHeaderSerializer, WebHeaderSerializer


class HeaderFactory:
    _map = {'mail': MailHeaderSerializer, 'mobile': MobileHeaderSerializer,
            'web': WebHeaderSerializer}

    @classmethod
    def serializer(cls, device: str):
        serializer_class = cls._map.get(device)
        return serializer_class
