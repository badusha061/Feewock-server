from rest_framework.serializers import ModelSerializer
from booking.models import Appointment , EmployeeAction
from rest_framework import serializers
from employee_auth.serializer import EmployeeSerializer
from employee_auth.models import Employees


class AppointmentSerializer(ModelSerializer):
    employee = EmployeeSerializer()
    class Meta:
        model = Appointment
        fields = ['id','employee','name' ,'user', 'phone_number' , 'location' , 'service_amount','date','service_time']



class AppointmentSerializerEmployee(ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id','employee','name' ,'user', 'phone_number' , 'location' , 'service_amount','date','service_time']


class EmployeeActionSerializer(ModelSerializer):
    comment = serializers.CharField(required=False)
    class Meta:
        model = EmployeeAction
        fields = ['id','appointment', 'action','comment']





class EmployeeActionSerializerAccept(ModelSerializer):
    comment = serializers.CharField(required=False)
    appointment = AppointmentSerializerEmployee()
    class Meta:
        model = EmployeeAction
        fields = ['id','appointment', 'action','comment']


class AppointmentSerializerUser(ModelSerializer):
    appointment  = AppointmentSerializer()
    class Meta:
        model = EmployeeAction
        fields = ['id','appointment', 'action','comment']
