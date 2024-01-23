from employee_auth.models import Employees
from rest_framework.serializers import ModelSerializer

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