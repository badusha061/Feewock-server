# Generated by Django 5.0.1 on 2024-02-07 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='phone_number',
            field=models.CharField(max_length=10),
        ),
    ]
