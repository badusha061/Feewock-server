# Generated by Django 5.0.1 on 2024-01-10 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_auth', '0004_employeepostion_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeepostion',
            name='postion_titile',
        ),
    ]
