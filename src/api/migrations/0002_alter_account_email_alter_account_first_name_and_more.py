# Generated by Django 4.2.2 on 2024-06-10 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='account',
            name='first_name',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='last_name',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='patronymic',
            field=models.CharField(blank=True, null=True, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='account',
            name='phone',
            field=models.CharField(blank=True, null=True, unique=True, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='user',
            name='passport_number',
            field=models.CharField(blank=True, null=True, verbose_name='Номер паспорта'),
        ),
        migrations.AlterField(
            model_name='user',
            name='place_of_birth',
            field=models.CharField(blank=True, null=True, verbose_name='Место рождения'),
        ),
        migrations.AlterField(
            model_name='user',
            name='registration_address',
            field=models.CharField(blank=True, null=True, verbose_name='Адрес регистрации'),
        ),
        migrations.AlterField(
            model_name='user',
            name='residential_address',
            field=models.CharField(blank=True, null=True, verbose_name='Адрес проживания'),
        ),
    ]
