from employee_auth.serializer import EmployeeSerializer , EmployeesListSerlizer
from employee_auth.models import Employees
from rest_framework.generics import ListAPIView


class ListEmployees(ListAPIView):
    serializer_class = EmployeeSerializer
    def get_queryset(self):
        servie_id = self.kwargs['service_id']
        return Employees.objects.filter(service = servie_id)