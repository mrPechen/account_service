from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    class Meta:
        db_table = 'account'
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    username = models.CharField(blank=True, null=True, unique=False)
    first_name = models.CharField(blank=True, null=True)
    last_name = models.CharField(blank=True, null=True)
    patronymic = models.CharField(verbose_name='Отчество', blank=True, null=True)
    phone = models.CharField(unique=True, verbose_name='Номер телефона', blank=True, null=True)
    email = models.EmailField(unique=True, verbose_name='Электронная почта', blank=True, null=True)

    USERNAME_FIELD = 'id'

    def __str__(self):
        return str(self.id)

class User(models.Model):
    class Meta:
        db_table = 'user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    account = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='user')
    birth_date = models.DateField(verbose_name='Дата рождения', blank=True, null=True)
    passport_number = models.CharField(verbose_name='Номер паспорта', blank=True, null=True)
    place_of_birth = models.CharField(verbose_name='Место рождения', blank=True, null=True)
    registration_address = models.CharField(verbose_name='Адрес регистрации', blank=True, null=True)
    residential_address = models.CharField(verbose_name='Адрес проживания', blank=True, null=True)

    def __str__(self):
        return str(self.account.id)