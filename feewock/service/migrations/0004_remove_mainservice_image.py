# Generated by Django 5.0.1 on 2024-01-09 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_alter_mainservice_is_active_alter_mainservice_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainservice',
            name='Image',
        ),
    ]
