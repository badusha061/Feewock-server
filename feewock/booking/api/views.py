from .serializer import AppointmentSerializer , EmployeeActionSerializer , AppointmentSerializerUser , AppointmentSerializerEmployee, EmployeeActionSerializerAccept
from rest_framework.generics import ListAPIView
from rest_framework.generics import ListCreateAPIView 
from booking.models import Appointment , EmployeeAction
from  rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from chat.utiles import notify_employee , notify_user
from user_auth.models import UserModel
from rest_framework.generics import RetrieveUpdateDestroyAPIView

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