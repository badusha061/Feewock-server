from rest_framework.generics import RetrieveUpdateDestroyAPIView , RetrieveUpdateAPIView , ListCreateAPIView
from employee_auth.models import Employees
from employee_auth.serializer import EmployeeSerializer
from .serializer import EmployeesIMageSerializers , EmployeesUpdateSerializers , EmployeesAvailabilitySerializers
from rest_framework.decorators import permission_classes 
from rest_framework.permissions import IsAuthenticated 
from EmployeeProfile.models import EmployeesAvailability

@permission_classes([IsAuthenticated])
class EmployeeUpdateImage(RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeesIMageSerializers
    queryset = Employees.objects.all()


@permission_classes([IsAuthenticated])
class EmployeeUpdate(RetrieveUpdateAPIView):
    serializer_class = EmployeesUpdateSerializers
    queryset = Employees.objects.all()


@permission_classes([IsAuthenticated])
class EmployeesAvailabilityView(ListCreateAPIView):
    serializer_class = EmployeesAvailabilitySerializers
    queryset = EmployeesAvailability.objects.all()