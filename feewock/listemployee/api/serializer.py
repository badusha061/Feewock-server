from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

class LocationSerializer(serializers.Serializer):
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()

