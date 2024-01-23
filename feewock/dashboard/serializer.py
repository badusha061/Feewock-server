from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from employee_auth.models import Employees
from service.serializer import SubServiceSerializer

class EmployeeIndvualSerializers(ModelSerializer):
    service = SubServiceSerializer(many = True)
    class Meta:
        model = Employees
        fields = ['id','username','email','gender','phone_number','dob','address','city','state','type_of_work','adhar_number','images','bank_details','is_active','service','location','role']
    read_only_fields = ["id"]