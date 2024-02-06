# Generated by Django 5.0.1 on 2024-02-06 04:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee_auth', '0026_remove_employees_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeesAvailability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('is_available', models.BooleanField(default=True)),
                ('employees', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_auth.employees')),
            ],
        ),
    ]
