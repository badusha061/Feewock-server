from .serializer import AppointmentSerializer , EmployeeActionSerializer 
from rest_framework.generics import ListAPIView
from rest_framework.generics import ListCreateAPIView 
from booking.models import Appointment , EmployeeAction
from  rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from chat.utiles import notify_employee , notify_user



@permission_classes([IsAuthenticated])
class appointment(ListCreateAPIView):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
    def perform_create(self, serializer):
        print('the create before')
        print('the create before')
        print('the create before')

        appointment = serializer.save()
        serializer_data = serializer.data 
        message = {
            'appointment_id':appointment.id,
            'appointment_details':serializer_data,
            'message':'New appointment created.'
        }

        print('the message  is  the', message)
        print('the message  is  the', message)
        print('the message  is  the', message)
        print('the message  is  the', message)
        print('the message  is  the', message)
        print('the message  is  the', message)
        print('the message  is  the', message)


        room_name = 'test'
        notify_employee(room_name , message)
        print('notifiy employeeee')
        print('notifiy employeeee')
        print('notifiy employeeee')
        print('notifiy employeeee')

        return appointment


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
        print('the create before')
        print('the create before')
        print('the create before')

        action = serializer.save()
        serializer_data = serializer.data 
        if serializer_data.action_details.action == 'accepted':

            print(serializer_data)
            print(serializer_data)
            print(serializer_data)

            message = {
                'action_id':action.id,
                'action_details':serializer_data,
                'message':'Your service is Accepted.'
            }
        else:
            print(serializer_data)
            print(serializer_data)
            print(serializer_data)

            message = {
                'action_id':action.id,
                'action_details':serializer_data,
                'message':'Your service is Rejected.'
            }


        print('the message  is  the', message)
        print('the message  is  the', message)
        print('the message  is  the', message)
        print('the message  is  the', message)
        print('the message  is  the', message)
        print('the message  is  the', message)
        print('the message  is  the', message)


        room_name = 'test'
        notify_user(room_name , message)
        print('notifiy employeeee')
        print('notifiy employeeee')
        print('notifiy employeeee')
        print('notifiy employeeee')

        return appointment

