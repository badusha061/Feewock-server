# Generated by Django 5.0.1 on 2024-01-13 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_auth', '0020_alter_employees_usermodel_ptr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employees',
            name='role',
        ),
    ]
