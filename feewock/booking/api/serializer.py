from rest_framework.serializers import ModelSerializer
from booking.models import Appointment , EmployeeAction
from rest_framework import serializers
from employee_auth.serializer import EmployeeSerializer
from employee_auth.models import Employees
from user_auth.api.serializer import UserIndvualSerializers
from chat.models import UserNotification , EmployeeNotification

class AppointmentSerializer(ModelSerializer):
    employee = EmployeeSerializer()
    class Meta:
        model = Appointment
        fields = ['id','employee','name' ,'user', 'phone_number' , 'location' , 'service_amount','date','service_time']


class AppointmentSerializerUserBook(ModelSerializer):
    employee = EmployeeSerializer()
    class Meta:
        model = Appointment
        fields = ['id','employee','name' ,'user', 'phone_number' , 'location' , 'service_amount','date','service_time','payment_method','payment_status','paid_at']


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
    appointment = AppointmentSerializer()
    class Meta:
        model = EmployeeAction
        fields = ['id','appointment', 'action','comment']


class AppointmentSerializerUser(ModelSerializer):
    appointment  = AppointmentSerializerUserBook()
    class Meta:
        model = EmployeeAction
        fields = ['id','appointment', 'action','comment']


class AppointmentSerializerAdmin(ModelSerializer):
    employee = EmployeeSerializer()
    user = UserIndvualSerializers()
    class Meta:
        model = Appointment
        fields = ['id','employee','name' ,'user', 'phone_number' , 'location' , 'service_amount','date','service_time','payment_method','payment_status','paid_at']




class UserNotificationSerializer(ModelSerializer):
    action = EmployeeActionSerializerAccept()
    class Meta:
        model = UserNotification
        fields = ['id','action','created_at']




class EmployeeNotificationSerializer(ModelSerializer):
    appointment = AppointmentSerializer()
    class Meta:
        model = EmployeeNotification
        fields = ['id','appointment','created_at']
