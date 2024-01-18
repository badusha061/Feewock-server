from rest_framework.serializers import ModelSerializer
from .models import MainService , SubService
from employee_auth.models import EmployeePostion
from rest_framework import serializers

class MainServiceSerializer(ModelSerializer):
    class Meta:
        model = MainService
        fields = ['id','name','is_active']
        read_only_fields = ["id"]


    def to_representation(self, instance):
        if instance is None:
            return None
        return super().to_representation(instance)


class SubServiceSerializerFetch(ModelSerializer):
    mainservice = MainServiceSerializer()
    class Meta:
       model = SubService
       fields = ['id','name','mainservice','Image']

   

class SubServiceSerializer(ModelSerializer):
    mainservice = serializers.PrimaryKeyRelatedField(queryset=MainService.objects.all())

    class Meta:
        model = SubService
        fields = ["id","name","mainservice", "Image"]



class EmployeePostionsSubService(ModelSerializer):
    class Meta:
        model = EmployeePostion
        fields = ['id','name', 'is_active']
    read_only_fields = ["id"]



class FetchMainService(ModelSerializer):
    subservice = SubServiceSerializerFetch(many = True, read_only=True)

    class Meta:
        model = MainService
        fields = ['name','subservice']