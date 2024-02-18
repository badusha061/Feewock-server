from rest_framework.serializers import ModelSerializer
from contact.models import ContactForm

class ContactFormSerializer(ModelSerializer):
    class Meta:
        model = ContactForm
        fields = ["id", "name", "email", "number","location","message"]