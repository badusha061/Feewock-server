# Generated by Django 5.0.1 on 2024-02-13 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_alter_appointment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='paid_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='payment_method',
            field=models.CharField(choices=[('ST', 'Stripe'), ('CO', 'Cash on Delivery')], default='ST', max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='payment_status',
            field=models.CharField(choices=[('PD', 'Pending'), ('PY', 'Paid'), ('FL', 'Failed')], default='PD', max_length=2, null=True),
        ),
    ]
