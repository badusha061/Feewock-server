from employee_auth.models import Employees
from rest_framework.serializers import ModelSerializer
from EmployeeProfile.models import EmployeesAvailability

class EmployeesIMageSerializers(ModelSerializer):
    class Meta:
        model = Employees 
        fields = ['id','images']
    read_only_fields = ["id"]



class EmployeesUpdateSerializers(ModelSerializer):
    class Meta:
        model = Employees 
        fields = ['id','username','email','gender','phone_number','dob','address','city','state','type_of_work','adhar_number','service','location','role','latitude','longitude']
    read_only_fields = ["id"]



class EmployeesAvailabilitySerializers(ModelSerializer):
    class Meta:
        model = EmployeesAvailability
        fields = ['id','employees','date','is_available']
    read_only_fields = ["id"]
