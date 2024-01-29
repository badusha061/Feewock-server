from .serializer import ChatSerializer , EmployeeChatSerializer
from rest_framework.generics import ListAPIView
from chat.models import Chat
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

@permission_classes([IsAuthenticated])
class GetMessage(ListAPIView):
    serializer_class = ChatSerializer
    def get_queryset(self):
        sender_id = self.kwargs['sender_id']
        reciever_id = self.kwargs['reciever_id']
        return Chat.objects.filter(sender__in =[sender_id , reciever_id] , receiver__in = [sender_id,reciever_id] )



@permission_classes([IsAuthenticated])
class GetEmployeeMessage(ListAPIView):
    serializer_class =EmployeeChatSerializer
    def get_queryset(self):
        employee_id = self.kwargs['pk']
        return Chat.objects.filter(receiver__in = [employee_id])
    