# Generated by Django 5.0.1 on 2024-01-15 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0007_rename_sub_name_subservice_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subservice',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]