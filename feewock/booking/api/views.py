from .serializer import AppointmentSerializer , EmployeeActionSerializer , AppointmentSerializerUser , AppointmentSerializerEmployee, EmployeeActionSerializerAccept , AppointmentSerializerAdmin
from rest_framework.generics import ListAPIView
from rest_framework.generics import ListCreateAPIView 
from booking.models import Appointment , EmployeeAction
from  rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from django.db.models import Q
from chat.utiles import notify_employee , notify_user
from user_auth.models import UserModel
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from booking.models import PaymentMethod , PaymentStatus
from rest_framework.response import Response
from rest_framework import status
# from booking.signals import send_payment_email_task
from booking.task import send_email_employee , send_email_user 
from django.http import HttpResponse


@permission_classes([IsAuthenticated])
class appointment(ListCreateAPIView):
    serializer_class = AppointmentSerializerEmployee
    queryset = Appointment.objects.all()
    def perform_create(self, serializer):
        appointment = serializer.save()
        serializer_data = serializer.data 
        message = {
            'appointment_id':appointment.id,
            'appointment_details':serializer_data,
            'message':'New appointment created.'
        }
        employee_id  = serializer_data['employee']
        notify_employee(employee_id , message)
        return appointment



# @permission_classes([IsAuthenticated]) 
class UserAppointment(ListAPIView):
    serializer_class = AppointmentSerializerUser
    def get_queryset(self):
        user_id = self.kwargs['pk']
        user = UserModel.objects.get(id = user_id )
        queryset = EmployeeAction.objects.filter(appointment__user = user)
        return queryset    


@permission_classes([IsAuthenticated]) 
class EmployeeAppointment(ListAPIView):
    serializer_class = AppointmentSerializer
    def get_queryset(self):
        employee_id = self.kwargs['pk']
        queryset = Appointment.objects.filter(employee = employee_id)
        return queryset
    
    

# @permission_classes([IsAuthenticated])
class EmployeeActionIndivual(ListAPIView):
    serializer_class = EmployeeActionSerializer
    def get_queryset(self):
        user_id = self.kwargs['pk']
        queryset = EmployeeAction.objects.filter(appointment__user=user_id)
        return queryset



@permission_classes([IsAuthenticated])
class EmployeeActionList(ListCreateAPIView):
    serializer_class = EmployeeActionSerializer
    queryset = EmployeeAction.objects.all()
    def perform_create(self, serializer):
        if not serializer.is_valid():
            print(serializer.errors)

        action = serializer.save()
        serializer_data = serializer.data 

        if 'action' in serializer_data:
            if serializer_data['action'] == 'accepted':
                message = {
                    'action_id':action.id,
                    'action_details':serializer_data,
                    'message':'Your service is Accepted.'
                }
            else:
                message = {
                    'action_id':action.id,
                    'action_details':serializer_data,
                    'message':'Your service is Rejected.'
                }
        room_name = 'test'
        notify_user(room_name , message)
        return appointment



@permission_classes([IsAuthenticated])
class IndivualAction(RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeActionSerializerAccept
    queryset = EmployeeAction.objects.all()




class Strip_Payment(APIView):
    def post(self , request , *args, **kwargs):
        try:
            appointment_id = self.kwargs['pk']
            appointment_instance = Appointment.objects.get(id = self.kwargs['pk'])
            appointment_instance.payment_status =  PaymentStatus.PAID
            appointment_instance.payment_method = PaymentMethod.STRIPE
            appointment_instance.marks_as_paid()
            appointment_instance.save()
            # send_payment_email_task.send(sender = Appointment , instance = appointment_id , created = True )
            send_email_user.delay(appointment_instance.id)
            send_email_employee.delay(appointment_instance.id)
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        


class CashOnDelivery(APIView):
    def post(self , request , *args, **kwargs):
        try:
            appointment_id = self.kwargs['pk']
            appointment_instance = Appointment.objects.get(id = self.kwargs['pk'])
            appointment_instance.payment_status =  PaymentStatus.PENDING
            appointment_instance.payment_method = PaymentMethod.COD
            appointment_instance.save()
            # send_payment_email_task.send(sender = Appointment , instance = appointment_id , created = True )
            send_email_user.delay(appointment_id)
            send_email_employee.delay(appointment_id)
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        



@permission_classes([IsAdminUser])
class AdminOrderList(ListCreateAPIView):
    serializer_class = AppointmentSerializerAdmin
    queryset = Appointment.objects.all()



@permission_classes([IsAdminUser])
class AdminOrderListIndivual(RetrieveUpdateDestroyAPIView):
    serializer_class = AppointmentSerializerAdmin
    queryset = Appointment.objects.all()


