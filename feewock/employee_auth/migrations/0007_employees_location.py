# Generated by Django 5.0.1 on 2024-01-11 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_auth', '0006_rename_postion_name_employeepostion_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='location',
            field=models.CharField(max_length=50, null=True),
        ),
    ]