from booking.models import Appointment , EmployeeAction
from django.db import models
from user_auth.models import UserModel
# Create your models here.

class Chat(models.Model):
    sender = models.ForeignKey( UserModel, on_delete=models.CASCADE , related_name = 'send_message')
    receiver = models.ForeignKey( UserModel, on_delete=models.CASCADE,related_name='receiver_message')
    message = models.TextField()
    thread_name = models.CharField(max_length=200 , null= True)
    date = models.DateTimeField(auto_now_add = True)
    is_read = models.BooleanField(default = False)


    
    def __str__(self) -> str:
        return f"{self.sender} - {self.receiver}"
    


class EmployeeNotification(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.appointment.employee.username



class UserNotification(models.Model):
    action = models.ForeignKey(EmployeeAction, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.action.action
   