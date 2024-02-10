from .serializer import ChatSerializer , EmployeeChatSerializer
from rest_framework.generics import ListAPIView , RetrieveUpdateDestroyAPIView
from chat.models import Chat
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework import status


@permission_classes([IsAuthenticated])
class GetMessage(ListAPIView):
    serializer_class = ChatSerializer
    def get_queryset(self):
        sender_id = self.kwargs['sender_id']
        reciever_id = self.kwargs['reciever_id']
        queryset = Chat.objects.filter(
            sender__in=[sender_id, reciever_id],
            receiver__in=[sender_id, reciever_id]
        ).order_by('date')
        for message in queryset:
            print(message.is_read)
            if message.receiver.id == self.request.user.id:
                message.is_read = True
                message.save()

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



@permission_classes([IsAuthenticated])
class GetEmployeeMessage(ListAPIView):
    serializer_class =EmployeeChatSerializer
    def get(self, request, *args, **kwargs):
        employee_id = self.kwargs['pk']
        dic = {}
        employee_chat = Chat.objects.filter(receiver__in = [employee_id])
        for chat in employee_chat:
            sender_id = chat.sender.id 
            sender_first_name = chat.sender.first_name
            sender_last_name = chat.sender.last_name
            sender_images = chat.sender.images if chat.sender.images else None
            if sender_id not in dic:
                dic[sender_id] = {
                    'id':sender_id,
                    'first_name':sender_first_name,
                    'last_name':sender_last_name,
                    'images':sender_images
                }
        data_list = list(dic.values())
        serializer  = self.serializer_class(data=data_list,many=True)
        try:
            serializer.is_valid(raise_exception=True)
            return Response(serializer.data)
        except serializers.ValidationError as e:
            return Response({"message": "serializer is not valid", "errors": e.detail})


