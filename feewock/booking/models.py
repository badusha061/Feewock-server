from django.db import models
from employee_auth.models import Employees
from user_auth.models import UserModel
# Create your models here.

class Appointment(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='appointments', null = True)
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE, related_name='employee')
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    location  = models.CharField(max_length=150)
    service_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    service_time = models.TimeField()
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

