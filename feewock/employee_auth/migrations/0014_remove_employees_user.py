# Generated by Django 5.0.1 on 2024-01-12 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_auth', '0013_employees_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employees',
            name='user',
        ),
    ]