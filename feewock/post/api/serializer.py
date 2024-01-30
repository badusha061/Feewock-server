from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from post.models import Posts , Likes
from employee_auth.serializer import EmployeeSerializer
from employee_auth.models import Employees

class PostSerializer(ModelSerializer):
    employee = serializers.PrimaryKeyRelatedField(queryset=Employees.objects.all())
    class Meta:
        model = Posts 
        fields = ['id','employee','created_at','image','captions']
    read_only_fields = ["id"]


class LikesSerializer(ModelSerializer):
    employee = serializers.PrimaryKeyRelatedField(queryset=Employees.objects.all())
    post = serializers.PrimaryKeyRelatedField(queryset=Posts.objects.all())

    class Meta:
        modal = Likes
        fields = ['id','employee','post']
    read_only_fields = ["id"]