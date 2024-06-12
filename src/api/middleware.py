from django.http import JsonResponse
from environs import Env


class DeviceHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == '/user/create/':
            env = Env()
            env.read_env()
            allowed_headers = env.list('ALLOWED_HEADERS', subcast=str)
            device_header = request.headers.get('x-Device')

            if device_header is None or device_header not in allowed_headers:
                return JsonResponse({'error': 'Invalid x-Device header'}, status=400)

        return self.get_response(request)
