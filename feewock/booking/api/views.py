from .serializer import *
from rest_framework.generics import ListAPIView
from rest_framework.generics import ListCreateAPIView 
from booking.models import Appointment , EmployeeAction , EmployeeStatus
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
from chat.models import UserNotification , EmployeeNotification



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
        count_result = EmployeeNotification.objects.filter(appointment__employee =employee_id ).count()
        total_count = int(count_result + 1)
        notify_employee(employee_id , message,total_count)
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
        apponitemnt_id = message['action_details']['appointment']
        print(message)
  
        app_instance = Appointment.objects.get(id = apponitemnt_id)
        user_instance = app_instance.user
        user = UserModel.objects.get(email = user_instance)
        user_id = user.id
        count_number  = UserNotification.objects.filter(action__appointment__user = user_instance).count()
        total_count = int(count_number + 1)
        notify_user(user_id , message, total_count)
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
            print('the appointment instance is the',appointment_instance.id)
            print('the appointment instance is the',appointment_instance.id)
            print('the appointment instance is the',appointment_instance.id)
            print('the appointment instance is the',appointment_instance.id)
            print('the appointment instance is the',appointment_instance.id)
            print('the appointment instance is the',appointment_instance.id)
            print('the appointment instance is the',appointment_instance.id)
            print('the appointment instance is the',appointment_instance.id)
            print('the appointment instance is the',appointment_instance.id)
            print('the appointment instance is the',appointment_instance.id)

            result1 = send_email_user.delay(appointment_instance.id)
            result2 = send_email_employee.delay(appointment_instance.id)
            print('status is the',result1.status)
            print('status is the',result2.status)
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
            print('send into to emails')
            print('send into to emails')
            print('send into to emails')
            print('send into to emails')
            print('send into to emails')
            print('send into to emails')
            print('send into to emails')
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



@permission_classes([IsAuthenticated])
class UserNotificationList(APIView):
    serializer_class = UserNotificationSerializer
    def get(self , request , *args, **kwargs):
        try:
            user_id = self.kwargs['pk']
            instance = UserModel.objects.get(id = user_id)
            notification_data = UserNotification.objects.filter(action__appointment__user = instance)
            print(notification_data)
            serializer = self.serializer_class(notification_data, many = True)
            return Response({"data":serializer.data })
        except Exception as e:
            return Response({"error":e})
        


@permission_classes([IsAuthenticated])
class EmployeeNotificationList(APIView):
    serializer_class = EmployeeNotificationSerializer
    def get(self , request , *args, **kwargs):
        try:
            employee_id = self.kwargs['pk']
            instance = Employees.objects.get(id = employee_id)
            notification_data = EmployeeNotification.objects.filter(appointment__employee = instance)
            print(notification_data)
            serializer = self.serializer_class(notification_data, many = True)
            return Response({"data":serializer.data })
        except Exception as e:
            return Response({"error":e})
        

@permission_classes([IsAuthenticated])
class DeleteUserNotification(APIView):
    def delete(self , request , *args, **kwargs):
        try:
            user_id = self.kwargs['pk']
            instance = UserModel.objects.get(id = user_id)
            UserNotification.objects.filter(action__appointment__user = instance).delete()
            return Response({"message":"Succesfully Deleted"})
        except Exception as e:
            return Response({"error":e})
        


@permission_classes([IsAuthenticated])
class DeleteEmployeeNotification(APIView):
    def delete(self , request , *args, **kwargs):
        try:
            employee_id = self.kwargs['pk']
            instance = Employees.objects.get(id = employee_id)
            EmployeeNotification.objects.filter(appointment__employee = instance).delete()
            return Response({"message":"Succesfully Deleted"})
        except Exception as e:
            return Response({"error":e})
        

@permission_classes([IsAuthenticated])
class EmployeeAppointmentList(APIView):
    serializer_class = AppointmentSerializerAdmin
    def get(self , request , *args, **kwargs):
        try:
            employee_id = self.kwargs['pk']
            instance = Employees.objects.get(id = employee_id)
            appointment_data = Appointment.objects.filter(employee = instance)
            serializers = self.serializer_class(appointment_data ,many= True)
            return Response(data=serializers.data , status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":e})



@permission_classes([IsAuthenticated])
class EmployeeAppointmentListIndivual(RetrieveUpdateDestroyAPIView):
    serializer_class = AppointmentSerializerAdmin
    queryset = Appointment.objects.all()
    

class EmployeeStausUpdate(APIView):
    def post(self , request , *args, **kwargs):
        try:
            app_id = self.kwargs['pk']
            data = request.data.get('status')
            appointment_data = Appointment.objects.get(id = app_id)
            if data == 1:
                appointment_data.employee_status = EmployeeStatus.COMING
                appointment_data.save()
            elif data == 2:
                appointment_data.employee_status = EmployeeStatus.ON_THE_WAY
                appointment_data.save()
            elif data == 3:
                appointment_data.employee_status = EmployeeStatus.NEAREST
                appointment_data.save()
            return Response( status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":e})