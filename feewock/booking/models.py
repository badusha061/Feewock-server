from django.db import models
from employee_auth.models import Employees
from user_auth.models import UserModel
from django.utils import timezone

# Create your models here.

class PaymentMethod(models.TextChoices):
    STRIPE = 'ST' , 'Stripe'
    COD = 'CO' , 'Cash on Delivery'
    PENDING = 'PD', 'Pending'

class PaymentStatus(models.TextChoices):
    PENDING = 'PD', 'Pending'
    PAID = 'PY' , 'Paid'
    FAILED = 'FL' , 'Failed'

class EmployeeStatus(models.TextChoices):
        COMING = 'coming', 'Coming'
        ON_THE_WAY = 'on_the_way', 'On the Way'
        NEAREST = 'nearest', 'Nearest'

class Appointment(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='appointments', null = True)
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE, related_name='employee')
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    location  = models.CharField(max_length=150)
    service_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    service_time = models.TimeField()
    payment_method = models.CharField(max_length = 2 , choices = PaymentMethod.choices , default = PaymentMethod.PENDING , null=True)
    payment_status = models.CharField(max_length = 2 , choices = PaymentStatus.choices , default = PaymentStatus.PENDING , null = True)
    paid_at = models.DateTimeField(null = True)
    employee_status = models.CharField(max_length = 10 , choices = EmployeeStatus.choices , default = EmployeeStatus.COMING, null=True)
    def marks_as_paid(self):
        self.status = PaymentStatus.PAID
        self.paid_at = timezone.now()
        self.save()


    def __str__(self) -> str:
        return self.name
    


class EmployeeAction(models.Model):
    ACCEPTED = 'accepted'
    REJECTED = 'rejected'
    PENDING =   'pending'
    ACTION_CHOICES = [
        (ACCEPTED, 'Accepted'),
        (REJECTED, 'Rejected'),
        (PENDING, 'Pending'),

    ]
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    action = models.CharField(max_length=50,choices = ACTION_CHOICES , default = PENDING )
    comment = models.TextField(blank= True, null = True)

    def __str__(self) -> str:
        return self.action

