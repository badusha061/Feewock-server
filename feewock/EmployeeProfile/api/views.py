from rest_framework.generics import RetrieveUpdateDestroyAPIView , RetrieveUpdateAPIView
from employee_auth.models import Employees
from employee_auth.serializer import EmployeeSerializer
from .serializer import EmployeesIMageSerializers , EmployeesUpdateSerializers

class EmployeeUpdateImage(RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeesIMageSerializers
    queryset = Employees.objects.all()


class EmployeeUpdate(RetrieveUpdateAPIView):
    serializer_class = EmployeesUpdateSerializers
    queryset = Employees.objects.all()