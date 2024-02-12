from django.db import models
from booking.models import Appointment
from django.utils import timezone
from user_auth.models import UserModel

# Create your models here.

class PaymentMethod(models.TextChoices):
    STRIPE = 'ST' , 'Stripe'
    COD = 'CO' , 'Cash on Delivery'


class PaymentStatus(models.TextChoices):
    PENDING = 'PD', 'Pending'
    PAID = 'PY' , 'Paid'
    FAILED = 'FL' , 'Failed'


class ServiceOrderPayment(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    method = models.CharField(max_length = 2 , choices = PaymentMethod.choices , default = PaymentMethod.STRIPE)
    status = models.CharField(max_length = 2 , choices = PaymentStatus.choices , default = PaymentStatus.PENDING)
    transaction_id = models.CharField(max_length=255 , blank = True , null = True)
    paid_at = models.DateTimeField(null = True)
    created_at = models.DateTimeField(auto_now_add = True)

    def marks_as_paid(self , transaction_id = None):
        self.status = PaymentStatus.PAID
        if transaction_id:
            self.transaction_id = transaction_id
        self.paid_at = timezone.now()
        self.save()

    def __str__(self) -> str:
        return self.method