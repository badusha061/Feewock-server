# Generated by Django 5.0.1 on 2024-02-07 04:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee_auth', '0026_remove_employees_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=10, unique=True)),
                ('location', models.CharField(max_length=150)),
                ('service_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
                ('service_time', models.TimeField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_auth.employees')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeAction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[('accepted', 'Accepted'), ('rejected', 'Rejected')], max_length=50)),
                ('comment', models.TextField(blank=True, null=True)),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.appointment')),
            ],
        ),
    ]
