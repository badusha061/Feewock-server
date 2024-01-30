from chat.models import Chat
from rest_framework.serializers import ModelSerializer
from user_auth.models import UserModel
from employee_auth.models import Employees

class UserChatSeralizer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id','email','first_name']


class EmployeeChatSeralizer(ModelSerializer):
    class Meta:
        model = Employees
        fields = ['id','email','username']

        
class ChatSerializer(ModelSerializer):
    sender = UserChatSeralizer(read_only = True)
    receiver = UserChatSeralizer(read_only = True)
    class Meta:
        model = Chat
        fields = ['id','sender','receiver','message','date','is_read']


        
class EmployeeChatSerializer(ModelSerializer):
    sender = UserChatSeralizer(read_only = True)
    receiver = EmployeeChatSeralizer(read_only = True)
    class Meta:
        model = Chat
        fields = ['id','sender','receiver']