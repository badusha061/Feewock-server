from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from post.models import Posts , Likes
from employee_auth.serializer import EmployeeSerializer
from employee_auth.models import Employees
from user_auth.models import UserModel

class EmployeeSerlizer(ModelSerializer):
    class Meta:
        model = Employees
        fields = ['id','username','images']


class PostSerializerUser(ModelSerializer):
    employee = EmployeeSerializer(read_only = True)
    class Meta:
        model = Posts 
        fields = ['id','employee','created_at','image','captions']
    read_only_fields = ["id"]


class PostSerializer(ModelSerializer):
    employee = serializers.PrimaryKeyRelatedField(queryset=Employees.objects.all())
    class Meta:
        model = Posts 
        fields = ['id','employee','created_at','image','captions']
    read_only_fields = ["id"]



class LikesSerializer(ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=UserModel.objects.all())
    post = serializers.PrimaryKeyRelatedField(queryset=Posts.objects.all())

    class Meta:
        model = Likes  
        fields = ['id', 'user', 'post']
        read_only_fields = ["id"]