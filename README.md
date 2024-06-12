Запуск:

Добавить данные для PostgreSQL в файл .env.example и убрать расширение example.
Из корня прокта запустить команду "docker-compose up -d".

Эндпоинты:

1. http://localhost:8000/api/user/create/ - POST. Обязательные поля:
  * Для заголовка x-Device = 'mail' - {"first_name": "first_name", "email": "email@example.ru"}
  * Для заголовка x-Device = 'mobile' - {"phone": "7ХХХХХХХХХХ"}
  * Для заголовка x-Device = 'web' - {
            'first_name': 'first_name',
            'last_name': 'last_name',
            'patronymic': 'patronymic',
            'phone': '7ХХХХХХХХХХ',
            'birth_date': '1990-01-01',
            'passport_number': '1234 567890',
            'place_of_birth': 'place_of_birth',
            'registration_address': 'registration_address'
        }
2. http://localhost:8000/api/user/{id}/ - GET. Получени юзера по id.
3. http://localhost:8000/api/user/search? - GET. Поиск юзера через query params. Поддерживаемые query params: first_name, last_name, patronymic, phone, email.
