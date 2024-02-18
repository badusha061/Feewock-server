from django.db import models

# Create your models here.

class ContactForm(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    number = models.CharField(max_length=10)
    location = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self) -> str:
        return self.name