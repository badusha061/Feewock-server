# Generated by Django 5.0.1 on 2024-01-10 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_auth', '0002_alter_employees_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeepostion',
            name='postion_name',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]
