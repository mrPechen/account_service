from django.http import JsonResponse


class DeviceHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == '/user/create/':
            allowed_headers = ['mail', 'mobile', 'web']
            device_header = request.headers.get('x-Device')

            if device_header is None or device_header not in allowed_headers:
                return JsonResponse({'error': 'Invalid x-Device header'}, status=400)

        return self.get_response(request)