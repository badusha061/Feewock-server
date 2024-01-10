from rest_framework.serializers import ModelSerializer
from .models import MainService , SubService

class MainServiceSerializer(ModelSerializer):
    class Meta:
        model = MainService
        fields = ['id','name','is_active']
        read_only_fields = ["id"]


    def to_representation(self, instance):
        if instance is None:
            return None
        return super().to_representation(instance)


class SubServiceSerializer(ModelSerializer):
    class Meta:
       model = SubService
       fields = ['id','name','Image','mainservice','is_active']
    read_only_fields = ["id"]

    def to_representation(self, instance):
        if instance is None:
            return None
        return super().to_representation(instance)