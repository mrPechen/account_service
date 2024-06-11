from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from api.models import Account, User


class UserModelAdmin(UserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("first_name", "last_name", "patronymic",
                           "email", "phone", "password1", "password2",),
            },
        ),
    )


@admin.register(Account)
class UserAdmin(UserModelAdmin):
    show_on_dispaly = '__all__'


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    show_on_dispaly = '__all__'
