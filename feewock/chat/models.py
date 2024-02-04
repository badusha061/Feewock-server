from django.db import models
from user_auth.models import UserModel
# Create your models here.

class Chat(models.Model):
    sender = models.ForeignKey( UserModel, on_delete=models.CASCADE , related_name = 'send_message')
    receiver = models.ForeignKey( UserModel, on_delete=models.CASCADE,related_name='receiver_message')
    message = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    is_read = models.BooleanField(default = False)


    def mark_as_read(self):
        self.is_read = True
        self.save()
    
    def __str__(self) -> str:
        return f"{self.sender} - {self.receiver}"
    


