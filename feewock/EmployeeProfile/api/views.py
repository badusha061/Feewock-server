from rest_framework.generics import RetrieveUpdateDestroyAPIView , RetrieveUpdateAPIView , ListCreateAPIView
from employee_auth.models import Employees
from employee_auth.serializer import EmployeeSerializer
from .serializer import EmployeesIMageSerializers , EmployeesUpdateSerializers , EmployeesAvailabilitySerializers
from rest_framework.decorators import permission_classes 
from rest_framework.permissions import IsAuthenticated 
from EmployeeProfile.models import EmployeesAvailability
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from chat.models import EmployeeNotification


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


@permission_classes([IsAuthenticated])
class EmployeesAvailabilityViewIndivual(ListCreateAPIView):
    serializer_class = EmployeesAvailabilitySerializers
    def get_queryset(self):
        id = self.kwargs['pk']
        return EmployeesAvailability.objects.filter(employees= id)
    


@permission_classes([IsAuthenticated])
class EmployeesAvailabilityViewIndivualDelete(RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeesAvailabilitySerializers
    queryset = EmployeesAvailability.objects.all()



@permission_classes([IsAuthenticated])
class NotificationCount(APIView):
    def get(self , request , *args, **kwargs):
        
        emp_id = int(self.kwargs['pk'])
        count_result = EmployeeNotification.objects.filter(appointment__employee =emp_id ).count()
        return Response(data=count_result , status=status.HTTP_200_OK)
    