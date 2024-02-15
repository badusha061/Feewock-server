from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from  django.conf import settings




  




@shared_task(bind = True)
def send_email_user(self , appointment_id):
    from booking.models import Appointment
    from user_auth.models import UserModel
    appointment_instance = Appointment.objects.get(id = appointment_id)
    user_intance = UserModel.objects.get(email = appointment_instance.user)
    subject = 'PAYMENT RECEIVED'
    full_name = f'{user_intance.first_name} {user_intance.last_name}'
    service_amount = appointment_instance.service_amount
    service_date = appointment_instance.date
    service_method = appointment_instance.payment_method
    email_from = settings.EMAIL_HOST_USER
    email_to = user_intance.email
    context ={
        "full_name":full_name,
        "service_amount":service_amount,
        "service_date":service_date,
        "service_method":service_method
    }
    html_messages = render_to_string("invoice.html",context=context)
    plain_message = strip_tags(html_messages)
    message = EmailMultiAlternatives(
        subject=subject,
        body=plain_message,
        from_email=email_from,
        to=[email_to]
    )
    message.attach_alternative(html_messages,"text/html")
    message.send()




@shared_task(bind = True)
def send_email_employee(self , appointment_id):
    from booking.models import Appointment
    from employee_auth.models import Employees
    appointment_instance = Appointment.objects.get(id = appointment_id)
    employee_instance = Employees.objects.get(username = appointment_instance.employee)
    username = employee_instance.username
    name = appointment_instance.name
    number = appointment_instance.phone_number
    location = appointment_instance.location
    service_amount = appointment_instance.service_amount
    service_date = appointment_instance.date
    service_time = appointment_instance.service_time
    service_method = appointment_instance.payment_method
    subject = 'YOUR BOOKED SERVICE'
    email_from = settings.EMAIL_HOST_USER
    email_to = employee_instance.email
    context ={
        "name":name,
        "number":number,
        "location":location,
        "service_amount":service_amount,
        "service_date":service_date,
        "service_time":service_time,
        "service_method":service_method,
        "username":username
    }
    html_messages = render_to_string("employeeEmail.html",context=context)
    plain_message = strip_tags(html_messages)
    message = EmailMultiAlternatives(
        subject=subject,
        body=plain_message,
        from_email=email_from,
        to=[email_to]
    )
    message.attach_alternative(html_messages,"text/html")
    message.send()
