from django.db.models import Q

from api.models import Account


class FilterService:

    @classmethod
    def search_users(cls, **kwargs):
        allowed_filters = ('first_name', 'last_name',
                           'patronymic', 'phone', 'email',)
        query = Q()

        for key, value in kwargs.items():
            if key in allowed_filters and value:
                query |= Q(**{f"{key}__icontains": value})
        return Account.objects.filter(query)
