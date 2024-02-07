from rest_framework.serializers import ModelSerializer
from booking.models import Appointment , EmployeeAction
from rest_framework import serializers

class AppointmentSerializer(ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id','employee','name' ,'user', 'phone_number' , 'location' , 'service_amount','date','service_time']


class EmployeeActionSerializer(ModelSerializer):
    comment = serializers.CharField(required=False)
    class Meta:
        model = EmployeeAction
        fields = ['id','appointment', 'action','comment']

