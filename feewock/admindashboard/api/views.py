from user_auth.models import UserModel
from employee_auth.models import Employees
from service.models  import SubService
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser
from booking.models import Appointment
from django.db.models import Sum
from booking.api.serializer import AppointmentSerializerAdmin

# @permission_classes([IsAdminUser])
class AdminDashboard(APIView):
    serializer_class = AppointmentSerializerAdmin
    def get(self , request):
        total_user = UserModel.objects.filter(role = 3).count()
        total_employee = UserModel.objects.filter(role = 2).count()
        total_service = SubService.objects.all().count()
        count_strip = Appointment.objects.filter(payment_method = 'ST').count()
        count_cashondelivery = Appointment.objects.filter(payment_method='CO').count()
        total_strip = Appointment.objects.filter(payment_method = 'ST').aggregate(Sum('service_amount'))['service_amount__sum'] or 0
        total_cashondelivery = Appointment.objects.filter(payment_method='CO').aggregate(Sum('service_amount'))['service_amount__sum'] or 0
        recend_history = Appointment.objects.filter(payment_method__in = ['ST', 'CO']).order_by('-id')[:5]
        serializer = self.serializer_class(recend_history , many= True)
        total_earnings  = total_strip + total_cashondelivery
        return Response({
            "total_user":total_user,
            "total_employee":total_employee,
            "total_service":total_service,
            "status": status.HTTP_200_OK,
            "total_cashondelivery":total_cashondelivery,
            "total_earnings":total_earnings,
            "total_strip":total_strip,
            "count_strip":count_strip,
            "count_cashondelivery":count_cashondelivery,
            "recend_history":recend_history,
            "recend_history":serializer.data
        })
