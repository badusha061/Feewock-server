# Generated by Django 5.0.1 on 2024-01-11 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('user_auth', '0006_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='group',
            field=models.ManyToManyField(related_name='user_model_permission', to='auth.permission'),
        ),
    ]
