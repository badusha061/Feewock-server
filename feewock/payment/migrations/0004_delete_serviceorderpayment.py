# Generated by Django 5.0.1 on 2024-02-13 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_rename_serviceorder_serviceorderpayment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ServiceOrderPayment',
        ),
    ]
