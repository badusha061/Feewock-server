# Generated by Django 5.0.1 on 2024-01-10 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_auth', '0003_alter_employeepostion_postion_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeepostion',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]