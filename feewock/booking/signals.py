from django.db.models.signals import post_save
from django.dispatch import receiver
from  .task import send_email_employee , send_email_user
from .models import Appointment


# @receiver(post_save , sender = Appointment)
# def send_payment_email_task(sender , instance ,created ,**kwargs):
#     print('calling signals')
#     print('calling signals')
#     print('calling signals')
#     print('calling signals')
#     print('calling signals')
#     print('calling signals')
#     print('calling signals')
#     print('calling signals')
#     print('calling signals')
#     print('calling signals')

#     if created:
#         print('it is created')
#         print('it is created')
#         print('it is created')
#         print('it is created')
#         print('it is created')
#         print('it is created')
#         print('it is created')
#         print('it is created')

#         send_email_employee(instance)
#         send_email_user(instance)