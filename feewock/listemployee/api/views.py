from employee_auth.serializer import EmployeeSerializer , EmployeesListSerlizer
from employee_auth.models import Employees
from rest_framework.generics import ListAPIView
from .serializer import LocationSerializer
from math import radians, cos, sin, asin, sqrt
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse

#calculate the two latitude and longitude for user and  employees
def distance(user_latitude, user_longitude, employee_latitude, employee_longitude):
    lon1 = radians(user_longitude)
    lon2 = radians(employee_longitude)
    lat1 = radians(user_latitude)
    lat2 = radians(employee_latitude)
    dlon = lon2 - lon1 
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 
    print('the c and r ',c * r)
    return c * r


class ListEmployees(ListAPIView):
    serializer_class = EmployeeSerializer
    def get_queryset(self):
        serializer  = LocationSerializer(data= self.request.query_params)
        if serializer.is_valid():
            servie_id = self.kwargs['service_id']
            validate_data = serializer.validated_data
            user_latitude = validate_data['latitude']
            user_longitude = validate_data['longitude']
            employee = Employees.objects.filter(service = servie_id)
            
            employee_distance = []
            for emp in employee:
                employee_latitude = emp.latitude
                employee_longitude = emp.longitude
                difference_betweeen = distance(user_latitude,user_longitude,employee_latitude,employee_longitude)
                employee_distance.append({
                     'employee_id':emp.id,
                     'distance_difference':difference_betweeen
                })
            sorted_employee_distance = sorted(employee_distance, key=lambda x: x['distance_difference'])
            sorted_ids = [ item['employee_id'] for item in  sorted_employee_distance]
            sorted_employee = Employees.objects.filter(id__in = sorted_ids)
          
            employee_dict = {employee.id: employee for employee in sorted_employee}
            ordered_employees = [employee_dict[employee_id] for employee_id in sorted_ids]

            return ordered_employees