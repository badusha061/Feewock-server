from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import OfferService
from service.serializer import SubServiceSerializer
from service.models import SubService

class OfferServiceSerializer(ModelSerializer):
    service = serializers.PrimaryKeyRelatedField(queryset=SubService.objects.all())

    class Meta:
        model = OfferService
        fields = '__all__'

class OfferServiceSerializerList(ModelSerializer):
    service = SubServiceSerializer()

    class Meta:
        model = OfferService
        fields = '__all__'