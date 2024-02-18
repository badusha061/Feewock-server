from rest_framework.generics import ListCreateAPIView
from .serializer import ContactFormSerializer
from contact.models import ContactForm
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser


class ContactFormUser(ListCreateAPIView):
    serializer_class = ContactFormSerializer
    queryset = ContactForm.objects.all()


@permission_classes([IsAdminUser])
class ContactFormAdmin(ListCreateAPIView):
    serializer_class = ContactFormSerializer
    queryset = ContactForm.objects.all()

