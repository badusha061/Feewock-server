from rest_framework.generics import RetrieveUpdateDestroyAPIView , RetrieveUpdateAPIView
from employee_auth.models import Employees
from employee_auth.serializer import EmployeeSerializer
from .serializer import EmployeesIMageSerializers , EmployeesUpdateSerializers
from rest_framework.decorators import permission_classes 
from rest_framework.permissions import IsAuthenticated 

@permission_classes([IsAuthenticated])
class EmployeeUpdateImage(RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeesIMageSerializers
    queryset = Employees.objects.all()


@permission_classes([IsAuthenticated])
class EmployeeUpdate(RetrieveUpdateAPIView):
    serializer_class = EmployeesUpdateSerializers
    queryset = Employees.objects.all()