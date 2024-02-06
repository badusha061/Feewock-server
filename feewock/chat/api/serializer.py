from chat.models import Chat
from rest_framework.serializers import ModelSerializer
from user_auth.models import UserModel
from employee_auth.models import Employees
from rest_framework import serializers

class UserChatSeralizer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id']


class EmployeeChatSeralizer(ModelSerializer):
    class Meta:
        model = Employees
        fields = ['id']

        
class ChatSerializer(ModelSerializer):
    sender = UserChatSeralizer(read_only = True)
    receiver = UserChatSeralizer(read_only = True)
    class Meta:
        model = Chat
        fields = ['id','sender','receiver','message','date','is_read']

        

class EmployeeChatSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    images = serializers.ImageField(allow_null=True, required=False)
    read_only_fields = ["id"]